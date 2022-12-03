"""
STUDENT: Antonio Santana
FILE: lab5.py

DESCRIPTION:
    This program demonstrates lab5 takes a port number of
    an existing node and a key (any value from column 1+4 of the file).

USAGE:
    python3 lab5.py

CODE ORGANIZATION:
    # Messages Section:
    # Node Section:
    # Helpers Section:
    # Main Section:
"""
import hashlib
import os
import socket
import time
from io import BytesIO
from random import randint

HDR_SZ = 24
NETWORK_MAGIC = b'\xf9\xbe\xb4\xd9'
TESTNET_NETWORK_MAGIC = b'\x0b\x11\x09\x07'

GENESIS_BLOCK = bytes.fromhex('0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c')
TESTNET_GENESIS_BLOCK = bytes.fromhex('0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4adae5494dffff001d1aa4ae18')
LOWEST_BITS = bytes.fromhex('ffff001d')

TWO_WEEKS = 60 * 60 * 24 * 14
MAX_TARGET = 0xffff * 256**(0x1d - 3)

class Block:

    def __init__(self, version, prev_block, merkle_root,
                 timestamp, bits, nonce, tx_hashes=None):
        self.version = version
        self.prev_block = prev_block
        self.merkle_root = merkle_root
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = nonce
        self.tx_hashes = tx_hashes

    @classmethod
    def parse(cls, s):
        '''Takes a byte stream and parses a block. Returns a Block object'''
        # s.read(n) will read n bytes from the stream
        # version - 4 bytes, little endian, interpret as int
        version = little_endian_to_int(s.read(4))
        # prev_block - 32 bytes, little endian (use [::-1] to reverse)
        prev_block = s.read(32)[::-1]
        # merkle_root - 32 bytes, little endian (use [::-1] to reverse)
        merkle_root = s.read(32)[::-1]
        # timestamp - 4 bytes, little endian, interpret as int
        timestamp = little_endian_to_int(s.read(4))
        # bits - 4 bytes
        bits = s.read(4)
        # nonce - 4 bytes
        nonce = s.read(4)
        # initialize class
        return cls(version, prev_block, merkle_root, timestamp, bits, nonce)

    def serialize(self):
        '''Returns the 80 byte block header'''
        # version - 4 bytes, little endian
        result = int_to_little_endian(self.version, 4)
        # prev_block - 32 bytes, little endian
        result += self.prev_block[::-1]
        # merkle_root - 32 bytes, little endian
        result += self.merkle_root[::-1]
        # timestamp - 4 bytes, little endian
        result += int_to_little_endian(self.timestamp, 4)
        # bits - 4 bytes
        result += self.bits
        # nonce - 4 bytes
        result += self.nonce
        return result

    def hash(self):
        '''Returns the hash256 interpreted little endian of the block'''
        # serialize
        s = self.serialize()
        # hash256
        h256 = hash256(s)
        # reverse
        return h256[::-1]

    def bip9(self):
        '''Returns whether this block is signaling readiness for BIP9'''
        # BIP9 is signalled if the top 3 bits are 001
        # remember version is 32 bytes so right shift 29 (>> 29) and see if
        # that is 001
        return self.version >> 29 == 0b001

    def bip91(self):
        '''Returns whether this block is signaling readiness for BIP91'''
        # BIP91 is signalled if the 5th bit from the right is 1
        # shift 4 bits to the right and see if the last bit is 1
        return self.version >> 4 & 1 == 1

    def bip141(self):
        '''Returns whether this block is signaling readiness for BIP141'''
        # BIP91 is signalled if the 2nd bit from the right is 1
        # shift 1 bit to the right and see if the last bit is 1
        return self.version >> 1 & 1 == 1

    def target(self):
        '''Returns the proof-of-work target based on the bits'''
        return bits_to_target(self.bits)

    def difficulty(self):
        '''Returns the block difficulty based on the bits'''
        # note difficulty is (target of lowest difficulty) / (self's target)
        # lowest difficulty has bits that equal 0xffff001d
        lowest = 0xffff * 256**(0x1d - 3)
        return lowest / self.target()

    def check_pow(self):
        '''Returns whether this block satisfies proof of work'''
        # get the hash256 of the serialization of this block
        h256 = hash256(self.serialize())
        # interpret this hash as a little-endian number
        proof = little_endian_to_int(h256)
        # return whether this integer is less than the target
        return proof < self.target()

    def validate_merkle_root(self):
        '''Gets the merkle root of the tx_hashes and checks that it's
        the same as the merkle root of this block.
        '''
        # reverse each item in self.tx_hashes
        hashes = [h[::-1] for h in self.tx_hashes]
        # compute the Merkle Root and reverse
        root = merkle_root(hashes)[::-1]
        # return whether self.merkle_root is the same
        return root == self.merkle_root


# Messages Section: Start
class NetworkEnvelope:
    """
    Network message container.
    """
    def __init__(self, command, payload, testnet=False):
        self.command = command
        self.payload = payload
        if testnet:
            self.magic = TESTNET_NETWORK_MAGIC
        else:
            self.magic = NETWORK_MAGIC

    def __repr__(self):
        return f"{self.command.decode('ascii')}: {self.payload.hex()}"

    @classmethod
    def parse(cls, s, testnet=False):
        """
        Takes a stream and creates a NetworkEnvelope.
        return an instance of the class
        """
        # check the network magic
        magic = s.read(4)
        if magic == b'':
            raise RuntimeError('Connection reset!')
        if testnet:
            expected_magic = TESTNET_NETWORK_MAGIC
        else:
            expected_magic = NETWORK_MAGIC
        if magic != expected_magic:
            raise RuntimeError(f'magic is not right {magic.hex()} vs {expected_magic.hex()}')
        # command 12 bytes
        command = s.read(12)
        # strip the trailing 0's
        command = command.strip(b'\x00')
        # payload length 4 bytes, little endian
        payload_length = little_endian_to_int(s.read(4))
        # checksum 4 bytes, first four of hash256 of payload
        checksum = s.read(4)
        # payload is of length payload_length
        payload = s.read(payload_length)
        # verify checksum
        calculated_checksum = hash256(payload)[:4]
        if calculated_checksum != checksum:
            raise RuntimeError('checksum does not match')
        return cls(command, payload, testnet=testnet)

    def serialize(self):
        """
        Returns the byte serialization of the entire network message.
        """
        # add the network magic
        result = self.magic
        # command 12 bytes
        # fill with 0's
        result += self.command + b'\x00' * (12 - len(self.command))
        # payload length 4 bytes, little endian
        result += int_to_little_endian(len(self.payload), 4)
        # checksum 4 bytes, first four of hash256 of payload
        result += hash256(self.payload)[:4]
        # payload
        result += self.payload
        return result

    def stream(self):
        """
        Returns a stream for parsing the payload.
        """
        return BytesIO(self.payload)

class VersionMessage:
    """
    Base Message container.
    https://developer.bitcoin.org/reference/p2p_networking.html#version
    The “version” message provides information about the transmitting node
    to the receiving node at the beginning of a connection. Until both peers
    have exchanged “version” messages, no other messages will be accepted.

    If a “version” message is accepted, the receiving node should send a “verack”
    message—but no node should send a “verack” message before initializing
    its half of the connection by first sending a “version” message.
    """
    command = b'version'

    def __init__(self, version=70015, services=0, timestamp=None,
                receiver_services=0,
                receiver_ip=b'\x00\x00\x00\x00', receiver_port=8333,
                sender_services=0,
                sender_ip=b'\x00\x00\x00\x00', sender_port=8333,
                nonce=None, user_agent=b'/cpsc5520distributedsystems:0.1/',
                latest_block=0, relay=False):
        self.version = version
        self.services = services
        if timestamp is None:
            self.timestamp = int(time.time())
        else:
            self.timestamp = timestamp
        self.receiver_services = receiver_services
        self.receiver_ip = receiver_ip
        self.receiver_port = receiver_port
        self.sender_services = sender_services
        self.sender_ip = sender_ip
        self.sender_port = sender_port
        if nonce is None:
            self.nonce = int_to_little_endian(randint(0, 2**64), 8)
        else:
            self.nonce = nonce
        self.user_agent = user_agent
        self.latest_block = latest_block
        self.relay = relay

    def serialize(self):
        """
        Serialize this message to send over the network.
        """
        # version is 4 bytes little endian
        result = int_to_little_endian(self.version, 4)
        # services is 8 bytes little endian
        result += int_to_little_endian(self.services, 8)
        # timestamp is 8 bytes little endian
        result += int_to_little_endian(self.timestamp, 8)
        # receiver services is 8 bytes little endian
        result += int_to_little_endian(self.receiver_services, 8)
        # IPV4 is 10 00 bytes and 2 ff bytes then receiver ip
        result += b'\x00' * 10 + b'\xff\xff' + bytearray((int(x) for x in self.receiver_ip.split('.')))
        # receiver port is 2 bytes, big endian
        result += self.receiver_port.to_bytes(2, 'big')
        # sender services is 8 bytes little endian
        result += int_to_little_endian(self.sender_services, 8)
        # IPV4 is 10 00 bytes and 2 ff bytes then sender ip
        result += b'\x00' * 10 + b'\xff\xff' + bytearray((int(x) for x in self.sender_ip.split('.')))
        # sender port is 2 bytes, big endian
        result += self.sender_port.to_bytes(2, 'big')
        # nonce should be 8 bytes
        result += self.nonce
        # useragent is a variable string, so varint first
        result += encode_varint(len(self.user_agent))
        result += self.user_agent
        # latest block is 4 bytes little endian
        result += int_to_little_endian(self.latest_block, 4)
        # relay is 00 if false, 01 if true
        if self.relay:
            result += b'\x01'
        else:
            result += b'\x00'
        return result

class VerAckMessage:
    """
    The “verack” message acknowledges a previously-received “version” message,
    informing the connecting node that it can begin to send other messages. The
    “verack” message has no payload; for an example of a message with no payload,
    see the message headers section.

    https://developer.bitcoin.org/reference/p2p_networking.html#verack
    """
    command = b'verack'

    def __init__(self):
        pass

    @classmethod
    def parse(cls, s):
        """Parse the verack stream."""
        return cls()

    def serialize(self):
        """Serialize the verack command."""
        return b''

class PingMessage:
    command = b'ping'

    def __init__(self, nonce):
        self.nonce = nonce

    @classmethod
    def parse(cls, s):
        nonce = s.read(8)
        return cls(nonce)

    def serialize(self):
        return self.nonce

class PongMessage:
    command = b'pong'

    def __init__(self, nonce):
        self.nonce = nonce

    def parse(cls, s):
        nonce = s.read(8)
        return cls(nonce)

    def serialize(self):
        return self.nonce

class GetHeadersMessage:
    """
    Get Headers Message class to define the getheaders command.
    We are we using the latest version, 70015.
    https://developer.bitcoin.org/reference/p2p_networking.html#protocol-versions
    """
    command = b'getheaders'

    def __init__(self, version=70015, num_hashes=1, start_block=None, end_block=None):
        self.version = version
        self.num_hashes = num_hashes
        if start_block is None:
            raise RuntimeError('a start block is required')
        self.start_block = start_block
        if end_block is None:
            self.end_block = b'\x00' * 32
        else:
            self.end_block = end_block

    def serialize(self):
        """
        Serialize this message to send over the network.
        """
        # protocol version is 4 bytes little-endian
        result = int_to_little_endian(self.version, 4)
        # number of hashes is a varint
        result += encode_varint(self.num_hashes)
        # start block is in little-endian
        result += self.start_block[::-1]
        # end block is also in little-endian
        result += self.end_block[::-1]
        return result

class HeadersMessage:
    """
    Headers Message class to define the headers command.s
    """
    command = b'headers'

    def __init__(self, blocks):
        self.blocks = blocks

    @classmethod
    def parse(cls, stream):
        # number of headers is in a varint
        num_headers = read_varint(stream)
        # initialize the blocks array
        blocks = []
        # loop through number of headers times
        for _ in range(num_headers):
            # add a block to the blocks array by parsing the stream
            blocks.append(Block.parse(stream))
            # read the next varint (num_txs)
            num_txs = read_varint(stream)
            # num_txs should be 0 or raise a RuntimeError
            if num_txs != 0:
                raise RuntimeError('number of txs not 0')
        # return a class instance
        return cls(blocks)

class GetDataMessage:
    """
    Get Data Message class to define the getdata command.
    """
    command = b'getdata'

    def __init__(self):
        self.data = []

    def add_data(self, data_type, identifier):
        """Appends the data."""
        self.data.append((data_type, identifier))

    def serialize(self):
        """
        Start with the number of items as a varint.
        """
        result = encode_varint(len(self.data))
        # loop through each tuple (data_type, identifier) in self.data
        for data_type, identifier in self.data:
            # data type is 4 bytes Little-Endian
            result += int_to_little_endian(data_type, 4)
            # identifier needs to be in Little-Endian
            result += identifier[::-1]
        return result
# Messages Section: Stop

# Node Section: Start
class Node:
    """
    Node to manage the communication.
    connect to socket
    Create a stream that we can use with the rest of the program.
    """
    def __init__(self, host, port=None, testnet=False, logging=False):
        if port is None:
            if testnet:
                port = 18333
            else:
                port = 8333
        self.testnet = testnet
        self.logging = logging
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.stream = self.socket.makefile('rb', None)
        if self.logging:
            print("\nClearing the Screen.")
            print("Create node, enable logging, and attempt to join the main network.\n\n")

    def handshake(self):
        """
        Do a handshake with the other node.Handshake is sending
        a version message and getting a verack back.
        create a version message
        send the command
        wait for a verack message
        """
        version = VersionMessage(receiver_ip=SOURCE_HOST,
                                 sender_ip=DESTINATION_HOST)
        if self.logging:
            print(f"Handshake with host {DESTINATION_HOST} on the main network.")
        self.send(version)
        self.wait_for(VerAckMessage)

    def send(self, message):
        """
        Send a message to the connected node.
        Create a network envelope
        Send the serialized envelope over the socket using sendall
        """
        envelope = NetworkEnvelope(
            message.command,
            message.serialize(),
            testnet=self.testnet)
        if self.logging:
            print(f'\nSending Network Message: {envelope}.\n')
            print(self.print_message(envelope.serialize()))
            # if envelope.command == VersionMessage.command:
                # print(self.print_version_msg(envelope.payload))
                # print(self.print_message(envelope.payload))
        self.socket.sendall(envelope.serialize())

    def read(self):
        """
        Read a message from the socket.
        """
        envelope = NetworkEnvelope.parse(self.stream, testnet=self.testnet)
        if self.logging:
            print(f'\nReceiving Network Message: {envelope}.\n')
        return envelope

    def wait_for(self, *message_classes):
        """
        Wait for one of the messages in the list.
        Initialize the command we have, which should be None
        return the envelope parsed as a member of the right message class
        """
        command = None
        command_to_class = {m.command: m for m in message_classes}

        # Loop until the command is in the commands we want
        while command not in command_to_class.keys():
            # get the next network message
            envelope = self.read()
            # set the command to be evaluated
            command = envelope.command
            # we know how to respond to version and ping, handle that here
            if command == VersionMessage.command:
                # send verack
                self.send(VerAckMessage())
            # elif command == PingMessage.command:
            #     # send pong
            #     self.send(PongMessage(envelope.payload))
        return command_to_class[command].parse(envelope.stream())

    def print_version_msg(self, b):
        """
        Report the contents of the given bitcoin version message (sans the header)
        :param payload: version message contents
        """
        # pull out fields
        version, my_services, epoch_time, your_services = b[:4], b[4:12], b[12:20], b[20:28]
        rec_host, rec_port, my_services2, my_host, my_port = b[28:44], b[44:46], b[46:54], b[54:70], b[70:72]
        nonce = b[72:80]
        user_agent_size, uasz = self.unmarshal_compactsize(b[80:])
        i = 80 + len(user_agent_size)
        user_agent = b[i:i + uasz]
        i += uasz
        start_height, relay = b[i:i + 4], b[i + 4:i + 5]
        extra = b[i + 5:]

        # print report
        prefix = '  '
        print(prefix + 'VERSION')
        print(prefix + '-' * 56)
        prefix *= 2
        print('{}{:32} version {}'.format(prefix, version.hex(), little_endian_to_int(version)))
        print('{}{:32} my services'.format(prefix, my_services.hex()))
        time_str = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(little_endian_to_int(epoch_time)))
        print('{}{:32} epoch time {}'.format(prefix, epoch_time.hex(), time_str))
        print('{}{:32} your services'.format(prefix, your_services.hex()))
        print('{}{:32} your host {}'.format(prefix, rec_host.hex(), self.ipv6_to_ipv4(rec_host)))
        print('{}{:32} your port {}'.format(prefix, rec_port.hex(), self.unmarshal_uint(rec_port)))
        print('{}{:32} my services (again)'.format(prefix, my_services2.hex()))
        print('{}{:32} my host {}'.format(prefix, my_host.hex(), self.ipv6_to_ipv4(my_host)))
        print('{}{:32} my port {}'.format(prefix, my_port.hex(), self.unmarshal_uint(my_port)))
        print('{}{:32} nonce'.format(prefix, nonce.hex()))
        print('{}{:32} user agent size {}'.format(prefix, user_agent_size.hex(), uasz))
        print('{}{:32} user agent \'{}\''.format(prefix, user_agent.hex(), str(user_agent, encoding='utf-8')))
        print('{}{:32} start height {}'.format(prefix, start_height.hex(), self.unmarshal_uint(start_height)))
        print('{}{:32} relay {}'.format(prefix, relay.hex(), bytes(relay) != b'\0'))
        if len(extra) > 0:
            print('{}{:32} EXTRA!!'.format(prefix, extra.hex()))
        elif len(extra) == 0:
            print('{}{:32} EXTRA'.format(prefix, extra.hex()))

    def print_message(self, msg, text=None):
        """
        Report the contents of the given bitcoin message
        :param msg: bitcoin message including header
        :return: message type
        """
        print('\n{}MESSAGE'.format('' if text is None else (text + ' ')))
        print('({}) {}'.format(len(msg), msg[:60].hex() + ('' if len(msg) < 60 else '...')))
        payload = msg[HDR_SZ:]
        command = self.print_header(msg[:HDR_SZ], checksum(payload))
        if command == 'version':
            self.print_version_msg(payload)
        # FIXME print out the payloads of other types of messages, too
        return command

    def print_header(self, header, expected_cksum=None):
        """
        Report the contents of the given bitcoin message header
        :param header: bitcoin message header (bytes or bytearray)
        :param expected_cksum: the expected checksum for this version message, if known
        :return: message type
        """
        magic, command_hex, payload_size, cksum = header[:4], header[4:16], header[16:20], header[20:]
        command = str(bytearray([b for b in command_hex if b != 0]), encoding='utf-8')
        psz = self.unmarshal_uint(payload_size)
        if expected_cksum is None:
            verified = ''
        elif expected_cksum == cksum:
            verified = '(verified)'
        else:
            verified = '(WRONG!! ' + expected_cksum.hex() + ')'
        prefix = '  '
        print(prefix + 'HEADER')
        print(prefix + '-' * 56)
        prefix *= 2
        print('{}{:32} magic'.format(prefix, magic.hex()))
        print('{}{:32} command: {}'.format(prefix, command_hex.hex(), command))
        print('{}{:32} payload size: {}'.format(prefix, payload_size.hex(), psz))
        print('{}{:32} checksum {}'.format(prefix, cksum.hex(), verified))
        return command

    def unmarshal_compactsize(self, b):
        """
        placeholder
        """
        key = b[0]
        if key == 0xff:
            return b[0:9], self.unmarshal_uint(b[1:9])
        if key == 0xfe:
            return b[0:5], self.unmarshal_uint(b[1:5])
        if key == 0xfd:
            return b[0:3], self.unmarshal_uint(b[1:3])
        return b[0:1], self.unmarshal_uint(b[0:1])

    def unmarshal_uint(self, b):
        """
        Returns the integer version of an array of bytes. The byte array
        is unsigned and the order is in little endian, the most
        significant byte is at the end.
        """
        return int.from_bytes(b, byteorder='little', signed=False)

    def ipv6_to_ipv4(self, ipv6):
        """
        Converts an IPv6 address to IPv4.
        """
        return '.'.join([str(b) for b in ipv6[12:]])
# Node Section: Stop

# Helpers Section: Start
def checksum(payload: bytes):
    """
    Calculate Bitcoin protocol checksum - first 4 bytes of
    sha256(sha256(payload)).
    :param payload: payload bytes
    :return: checksum
    """
    return hash256(payload)[:4]

def ipv6_from_ipv4(ipv4_str):
    """
    Converts an IPv4 address to IPv6.
    """
    pchIPv4 = bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xff, 0xff])
    return pchIPv4 + bytearray((int(x) for x in ipv4_str.split('.')))

def hash256(s):
    """
    Two rounds of sha256.
    """
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()

def little_endian_to_int(b):
    """
    Little_endian_to_int takes byte sequence as a little-endian number.
    Returns an integer.
    """
    return int.from_bytes(b, 'little')

def int_to_little_endian(n, length):
    """
    Endian_to_little_endian takes an integer and returns the little-endian
    byte sequence of length.
    """
    return n.to_bytes(length, 'little')

def read_varint(s):
    """
    Read_varint reads a variable integer from a stream.
    """
    i = s.read(1)[0]
    if i == 0xfd:
        # 0xfd means the next two bytes are the number
        return little_endian_to_int(s.read(2))
    elif i == 0xfe:
        # 0xfe means the next four bytes are the number
        return little_endian_to_int(s.read(4))
    elif i == 0xff:
        # 0xff means the next eight bytes are the number
        return little_endian_to_int(s.read(8))
    else:
        # anything else is just the integer
        return i

def encode_varint(i):
    """
    Encodes an integer as a varint.
    """
    if i < 0xfd:
        return bytes([i])
    elif i < 0x10000:
        return b'\xfd' + int_to_little_endian(i, 2)
    elif i < 0x100000000:
        return b'\xfe' + int_to_little_endian(i, 4)
    elif i < 0x10000000000000000:
        return b'\xff' + int_to_little_endian(i, 8)
    else:
        raise ValueError('integer too large: {}'.format(i))

def target_to_bits(target):
    '''Turns a target integer back into bits, which is 4 bytes'''
    raw_bytes = target.to_bytes(32, 'big')
    # get rid of leading 0's
    raw_bytes = raw_bytes.lstrip(b'\x00')
    if raw_bytes[0] > 0x7f:
        # if the first bit is 1, we have to start with 00
        exponent = len(raw_bytes) + 1
        coefficient = b'\x00' + raw_bytes[:2]
    else:
        # otherwise, we can show the first 3 bytes
        # exponent is the number of digits in base-256
        exponent = len(raw_bytes)
        # coefficient is the first 3 digits of the base-256 number
        coefficient = raw_bytes[:3]
    # we've truncated the number after the first 3 digits of base-256
    new_bits = coefficient[::-1] + bytes([exponent])
    return new_bits

def calculate_new_bits(previous_bits, time_differential):
    '''Calculates the new bits given
    a 2016-block time differential and the previous bits'''
    # if the time differential is greater than 8 weeks, set to 8 weeks
    if time_differential > TWO_WEEKS * 4:
        time_differential = TWO_WEEKS * 4
    # if the time differential is less than half a week, set to half a week
    if time_differential < TWO_WEEKS // 4:
        time_differential = TWO_WEEKS // 4
    # the new target is the previous target * time differential / two weeks
    new_target = bits_to_target(previous_bits) * time_differential // TWO_WEEKS
    # if the new target is bigger than MAX_TARGET, set to MAX_TARGET
    if new_target > MAX_TARGET:
        new_target = MAX_TARGET
    # convert the new target to bits
    return target_to_bits(new_target)

def merkle_parent(hash1, hash2):
    '''Takes the binary hashes and calculates the hash256'''
    # return the hash256 of hash1 + hash2
    return hash256(hash1 + hash2)

def merkle_parent_level(hashes):
    '''Takes a list of binary hashes and returns a list that's half
    the length'''
    # if the list has exactly 1 element raise an error
    if len(hashes) == 1:
        raise RuntimeError('Cannot take a parent level with only 1 item')
    # if the list has an odd number of elements, duplicate the last one
    # and put it at the end so it has an even number of elements
    if len(hashes) % 2 == 1:
        hashes.append(hashes[-1])
    # initialize next level
    parent_level = []
    # loop over every pair (use: for i in range(0, len(hashes), 2))
    for i in range(0, len(hashes), 2):
        # get the merkle parent of the hashes at index i and i+1
        parent = merkle_parent(hashes[i], hashes[i + 1])
        # append parent to parent level
        parent_level.append(parent)
    # return parent level
    return parent_level

def merkle_root(hashes):
    '''Takes a list of binary hashes and returns the merkle root
    '''
    # current level starts as hashes
    current_level = hashes
    # loop until there's exactly 1 element
    while len(current_level) > 1:
        # current level becomes the merkle parent level
        current_level = merkle_parent_level(current_level)
    # return the 1st item of the current level
    return current_level[0]

def bits_to_target(bits):
    '''Turns bits into a target (large 256-bit integer)'''
    # last byte is exponent
    exponent = bits[-1]
    # the first three bytes are the coefficient in little endian
    coefficient = little_endian_to_int(bits[:-1])
    # the formula is:
    # coefficient * 256**(exponent-3)
    return coefficient * 256**(exponent - 3)

def clear_screen():
    """Define our clear function for Windows, Mac, and Linux."""
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
# Helpers Section: Stop

# Main Section:
if __name__ == '__main__':
    clear_screen()
    SOURCE_HOST = "127.0.0.1"
    # DESTINATION_HOST = "89.234.180.194"
    DESTINATION_HOST = "97.126.42.129"
    # DESTINATION_HOST = "97-126-42-129.tukw.qwest.net"
    # DESTINATION_HOST = "81.171.22.143"

    # Block number from command line argument 
    block_number = 1085

    previous = Block.parse(BytesIO(GENESIS_BLOCK))
    first_epoch_timestamp = previous.timestamp
    expected_bits = LOWEST_BITS
    count = 1
    node = Node(host=DESTINATION_HOST, logging=True)
    node.handshake()
    for _ in range(19):
        getheaders = GetHeadersMessage(start_block=previous.hash())
        node.send(getheaders)
        headers = node.wait_for(HeadersMessage)
        # for header in headers.blocks:
        #     if block_number == header.block_number:
        #         print(f"Found my block number {header.block_number}")
        #     # if not header.check_pow():
        #     #     raise RuntimeError('bad PoW at block {}'.format(count))
        #     # if header.prev_block != previous.hash():
        #     #     raise RuntimeError('discontinuous block at {}'.format(count))
        #     # if count % 2016 == 0:
        #     #     time_diff = previous.timestamp - first_epoch_timestamp
        #     #     expected_bits = calculate_new_bits(previous.bits, time_diff)
        #     #     print(expected_bits.hex())
        #     #     first_epoch_timestamp = header.timestamp
        #     # if header.bits != expected_bits:
        #     #     raise RuntimeError('bad bits at block {}'.format(count))
        #     previous = header
        #     count += 1