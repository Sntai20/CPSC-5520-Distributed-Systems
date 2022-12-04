"""
STUDENT: Antonio Santana
FILE: lab5.py

DESCRIPTION:
    This program demonstrates lab5 using the node class to manage all the interactions with
    the Bitcoin network. The node connects to a peer in the P2P BitCoin network and gets
    the block number that corresponds to my SU ID number (modulo 10,000).
    
    In this lab, I attempted to get as much of the extra credit as possible, including "display
    the transactions in the block." and "working with the merkle-tree to manipulate one of the
    transactions in the block to change its output account, then fix up the block to correctly
    represent this modified data (fix the merkle-tree hashes, etc.). Then show with a
    program-generated report how the hash of the block has changed and the ways in which this
    block would be rejected by peers in the network."

USAGE:
    python3 lab5.py

CODE ORGANIZATION:
    # Messages Section:
    # Node Section:
    # Helpers Section:
    # Main Section:

EXPECTED OUTPUT:

Clearing the Screen.
Create node, enable logging, and attempt to join the main network.


Handshake with host 89.234.180.194 on the main network.

Sending Network Message: version: 7f110100000000000000000024378c6300000000000000000000000000000000000000000000ffff7f000001208d000000000000000000000000000000000000ffff59eab4c2208db668f6844056e66a202f6370736335353230646973747269627574656473797374656d733a302e312f0000000000.

MESSAGE
(142) f9beb4d976657273696f6e00000000007600000088e0345b7f110100000000000000000024378c630000000000000000000000000000000000000000...
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    76657273696f6e0000000000         command: version
    76000000                         payload size: 118
    88e0345b                         checksum (verified)
  VERSION
  --------------------------------------------------------
    7f110100                         version 70015
    0000000000000000                 my services
    24378c6300000000                 epoch time Sun, 04 Dec 2022 05:59:00 GMT
    0000000000000000                 your services
    00000000000000000000ffff7f000001 your host 127.0.0.1
    208d                             your port 8333
    0000000000000000                 my services (again)
    00000000000000000000ffff59eab4c2 my host 89.234.180.194
    208d                             my port 8333
    b668f6844056e66a                 nonce
    20                               user agent size 32
    2f6370736335353230646973747269627574656473797374656d733a302e312f user agent '/cpsc5520distributedsystems:0.1/'
    00000000                         start height 0
    00                               relay False
                                     EXTRA
version

Receiving Network Message: b'version'.

MESSAGE
(127) f9beb4d976657273696f6e000000000067000000178fe54480110100090400000000000028378c630000000000000000000000000000000000000000...
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    76657273696f6e0000000000         command: version
    67000000                         payload size: 103
    178fe544                         checksum (verified)
  VERSION
  --------------------------------------------------------
    80110100                         version 70016
    0904000000000000                 my services
    28378c6300000000                 epoch time Sun, 04 Dec 2022 05:59:04 GMT
    0000000000000000                 your services
    00000000000000000000ffff4c935d47 your host 76.147.93.71
    fac6                             your port 50938
    0904000000000000                 my services (again)
    00000000000000000000000000000000 my host 0.0.0.0
    0000                             my port 0
    72033920026e7bab                 nonce
    11                               user agent size 17
    2f5361746f7368693a32322e39392e302f user agent '/Satoshi:22.99.0/'
    74af0b00                         start height 765812
    01                               relay True
                                     EXTRA
version
Peer height: 765812

Sending Network Message: verack: .

MESSAGE
(24) f9beb4d976657261636b000000000000000000005df6e0e2
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    76657261636b000000000000         command: verack
    00000000                         payload size: 0
    5df6e0e2                         checksum (verified)
verack

Receiving Network Message: b'verack'.


MESSAGE
(24) f9beb4d976657261636b000000000000000000005df6e0e2
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    76657261636b000000000000         command: verack
    00000000                         payload size: 0
    5df6e0e2                         checksum (verified)
verack
Lookup Block Number: 1085 Peer height: 765812

Sending Network Message: getheaders: 7f110100016fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d61900000000000000000000000000000000000000000000000000000000000000000000000000.

MESSAGE
(93) f9beb4d96765746865616465727300004500000084f4958d7f110100016fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d61900000000...
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    676574686561646572730000         command: getheaders
    45000000                         payload size: 69
    84f4958d                         checksum (verified)
getheaders

Receiving Network Message: b'sendheaders'.


MESSAGE
(24) f9beb4d973656e646865616465727300000000005df6e0e2
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    73656e646865616465727300         command: sendheaders
    00000000                         payload size: 0
    5df6e0e2                         checksum (verified)
sendheaders

Receiving Network Message: b'sendcmpct'.


MESSAGE
(33) f9beb4d973656e64636d70637400000009000000e92f5ef8000200000000000000
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    73656e64636d706374000000         command: sendcmpct
    09000000                         payload size: 9
    e92f5ef8                         checksum (verified)
    00                               announce: False
    0200000000000000                 version: 2
sendcmpct

Receiving Network Message: b'sendcmpct'.


MESSAGE
(33) f9beb4d973656e64636d70637400000009000000ccfe104a000100000000000000
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    73656e64636d706374000000         command: sendcmpct
    09000000                         payload size: 9
    ccfe104a                         checksum (verified)
    00                               announce: False
    0100000000000000                 version: 1
sendcmpct

Receiving Network Message: b'ping'.


MESSAGE
(32) f9beb4d970696e670000000000000000080000000c35dc778546929f272fd779
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    70696e670000000000000000         command: ping
    08000000                         payload size: 8
    0c35dc77                         checksum (verified)
ping

Receiving Network Message: b'feefilter'.


MESSAGE
(32) f9beb4d966656566696c74657200000008000000e80fd19fe803000000000000
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    66656566696c746572000000         command: feefilter
    08000000                         payload size: 8
    e80fd19f                         checksum (verified)
    e803000000000000                 count: 1000
feefilter

Receiving Network Message: b'headers'.


MESSAGE
(162027) f9beb4d9686561646572730000000000d3780200a65b2b77fdd007010000006fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000...
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    686561646572730000000000         command: headers
    d3780200                         payload size: 162003
    a65b2b77                         checksum (verified)
headers

Sending Network Message: getdata: 00.


MESSAGE
(25) f9beb4d9676574646174610000000000010000001406e05800
  HEADER
  --------------------------------------------------------
    f9beb4d9                         magic
    676574646174610000000000         command: getdata
    01000000                         payload size: 1
    1406e058                         checksum (verified)
    00                               count: 0
getdata
Block Hash: 7c2bac1d1d00ffff495fab294a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b000000000000000000000000000000000000000000000000000000000000000000000001
"""
import hashlib
import os
import socket
import time
from io import BytesIO
from random import randint

HEADER_SIZE = 24
NETWORK_MAGIC = b'\xf9\xbe\xb4\xd9'
TESTNET_NETWORK_MAGIC = b'\x0b\x11\x09\x07'

GENESIS_BLOCK = bytes.fromhex('0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c')
TESTNET_GENESIS_BLOCK = bytes.fromhex('0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4adae5494dffff001d1aa4ae18')
LOWEST_BITS = bytes.fromhex('ffff001d')

TWO_WEEKS = 60 * 60 * 24 * 14
MAX_TARGET = 0xffff * 256**(0x1d - 3)

PREFIX = '  '

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
        """Takes a byte stream and parses a block. Returns a Block object"""
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
        """Returns the 80 byte block header"""
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
        """Returns the hash256 interpreted little endian of the block"""
        # serialize
        s = self.serialize()
        # hash256
        h256 = hash256(s)
        # reverse
        return h256[::-1]

    def bip9(self):
        """Returns whether this block is signaling readiness for BIP9"""
        # BIP9 is signalled if the top 3 bits are 001
        # remember version is 32 bytes so right shift 29 (>> 29) and see if
        # that is 001
        return self.version >> 29 == 0b001

    def bip91(self):
        """Returns whether this block is signaling readiness for BIP91"""
        # BIP91 is signalled if the 5th bit from the right is 1
        # shift 4 bits to the right and see if the last bit is 1
        return self.version >> 4 & 1 == 1

    def bip141(self):
        """Returns whether this block is signaling readiness for BIP141"""
        # BIP91 is signalled if the 2nd bit from the right is 1
        # shift 1 bit to the right and see if the last bit is 1
        return self.version >> 1 & 1 == 1

    def target(self):
        """Returns the proof-of-work target based on the bits"""
        return bits_to_target(self.bits)

    def difficulty(self):
        """Returns the block difficulty based on the bits"""
        # note difficulty is (target of lowest difficulty) / (self's target)
        # lowest difficulty has bits that equal 0xffff001d
        lowest = 0xffff * 256**(0x1d - 3)
        return lowest / self.target()

    def check_pow(self):
        """Returns whether this block satisfies proof of work"""
        # get the hash256 of the serialization of this block
        h256 = hash256(self.serialize())
        # interpret this hash as a little-endian number
        proof = little_endian_to_int(h256)
        # return whether this integer is less than the target
        return proof < self.target()

    def validate_merkle_root(self):
        """Gets the merkle root of the tx_hashes and checks that it's
        the same as the merkle root of this block.
        """
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
    The “version” message provides information about the transmitting node
    to the receiving node at the beginning of a connection. Until both peers
    have exchanged “version” messages, no other messages will be accepted.

    If a “version” message is accepted, the receiving node should send a “verack”
    message—but no node should send a “verack” message before initializing
    its half of the connection by first sending a “version” message.

    https://developer.bitcoin.org/reference/p2p_networking.html#version
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

    def parse(self, cls, s):
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
    Headers Message class to define the headers command.
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
    def __init__(self, host, port=None, testnet=False, block_number=None, logging=False):
        if port is None:
            if testnet:
                port = 18333
            else:
                port = 8333
        self.testnet = testnet
        self.block_number = int(block_number)
        self.logging = logging
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.stream = self.socket.makefile('rb', None)
        self.peer_height = None
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
        self.socket.sendall(envelope.serialize())

    def read(self):
        """Read a message from the socket."""
        envelope = NetworkEnvelope.parse(self.stream, testnet=self.testnet)
        if self.logging:
            print(f'\nReceiving Network Message: {envelope.command}.\n')
            print(self.print_message(envelope.serialize()))
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
                # get the height
                self.peer_height = self.unmarshal_uint(envelope.serialize()[-5:-1])
                print(f"Peer height: {self.peer_height}")
                # send verack
                self.send(VerAckMessage())
            
        return command_to_class[command].parse(envelope.stream())

    def lookup_block_number(self):
        time.sleep(3)
        # Check supplied block number against peer's blockchain height
        if self.block_number > self.peer_height:
            print('\nCould not retrieve block {}: max height is {}'.format(self.block_number, self.peer_height))
            exit(1)

        print(f"Lookup Block Number: {self.block_number} Peer height: {self.peer_height}")
        previous = Block.parse(BytesIO(GENESIS_BLOCK))
        
        getheaders = GetHeadersMessage(start_block=previous.hash())
        node.send(getheaders)
        headers = node.wait_for(HeadersMessage)
        getdata = GetDataMessage()
        node.send(getdata)

        # Send getblocks (starting from genesis) -> receive inv
        block_hash = self.swap_endian(GENESIS_BLOCK)
        print(f"Block Hash: {block_hash.hex()}")
        current_height = 0
        # Store 500 blocks from inv messages
        # last_500_blocks = []
        # Keep sending getblocks until inventory has the desired block number
        # while current_height < self.block_number:
        #     print(f"Current_height {current_height} is less than our block_number {self.block_number}")
        #     last_500_blocks, current_height = self.send_getblocks_message(block_hash, current_height)
        #     block_hash = last_500_blocks[-1]

        # my_block_hash = last_500_blocks[(self.block_number - 1) % 500]
        # getdata_bytes = self.build_message('getdata', self.getdata_message(2, my_block_hash))
        # msg_list = self.exchange_messages(getdata_bytes, height=self.block_number, wait=True)
        # my_block = b''.join(msg_list)

    def send_getblocks_message(self, input_hash, current_height):
        """
        Helper method for sending the getblocks message to the Bitcoin node.
        :param input_hash: locator hash for the getblocks message
        :param current_height: local blockchain height
        :return: list of last 500 block headers, updated height
        """
        getblocks_bytes = self.build_message('getblocks', self.getblocks_message(input_hash))
        peer_inv = self.exchange_messages(getblocks_bytes, expected_bytes=18027, height=current_height + 1)
        peer_inv_bytes = b''.join(peer_inv)
        last_500_headers = [peer_inv_bytes[i:i + 32] for i in range(31, len(peer_inv_bytes), 36)]
        current_height = self.update_current_height(peer_inv, current_height)
        return last_500_headers, current_height

    # Encapsulate all of this.
    def build_message(self, command, payload):
        """
        Returns the complete message bytes (header + payload).
        :param command: message/command type
        :param payload: payload of the message
        :return: complete message bytes
        """
        return self.message_header(command, payload) + payload

    def exchange_messages(self, bytes_to_send, expected_bytes=None, height=None, wait=False):
        """
        Exchanges messages with the Bitcoin node and prints the messages that
        are being sent and received.
        :param bytes_to_send: bytes to send to BTC node
        :param expected_bytes: number of bytes expecting to receive
        :param height: local blockchain height
        :param wait: whether to wait for a response
        :return: list of the message bytes received
        """
        BUFFER_SIZE = 64000  # sock recv argument
        
        self.socket.settimeout(0.5)
        bytes_received = b''

        try:
            self.socket.sendall(bytes_to_send)

            if expected_bytes:
                # Message size is fixed: receive until byte sizes match
                while len(bytes_received) < expected_bytes:
                    bytes_received += self.socket.recv(BUFFER_SIZE)
            elif wait:
                # Message size could vary: wait until timeout to receive all bytes
                while True:
                    bytes_received += self.socket.recv(BUFFER_SIZE)

        except Exception as e:
            print('\nNo bytes left to receive {}'
                .format(str(e)))

        finally:
            peer_msg_list = self.split_message(bytes_received)
            return peer_msg_list

    def update_current_height(self, block_list, curr_height):
        """
        Update the current height of our local block chain.
        :param block_list: list of blocks
        :param curr_height: before height
        :return: after height
        """
        return curr_height + (len(block_list[-1]) - 27) // 36

    def swap_endian(self, b: bytes):
        """
        Swap the endianness of the given bytes. If little, swaps to big. If big,
        swaps to little.
        :param b: bytes to swap
        :return: swapped bytes
        """
        swapped = bytearray.fromhex(b.hex())
        swapped.reverse()
        return swapped

    def split_message(self, peer_msg_bytes):
        """
        Splits the bytes into a list of each individual message.
        :param peer_msg_bytes: message bytes to split
        :return: list of each message
        """
        msg_list = []
        while peer_msg_bytes:
            payload_size = self.unmarshal_uint(peer_msg_bytes[16:20])
            msg_size = HEADER_SIZE + payload_size
            msg_list.append(peer_msg_bytes[:msg_size])
            
            # Discard to move onto next message
            peer_msg_bytes = peer_msg_bytes[msg_size:]
        return msg_list

    def message_header(self, command, payload):
        """
        Builds a Bitcoin message header.
        :param command: command/message type
        :param payload: payload of the message
        :return: message header bytes
        """
        START_STRING = bytes.fromhex('f9beb4d9')  # Magic bytes
        COMMAND_SIZE = 12  # Message command length
        magic = START_STRING
        command_name = command.encode('ascii')
        while len(command_name) < COMMAND_SIZE:
            command_name += b'\0'
        payload_size = self.uint32_t(len(payload))
        check_sum = checksum(payload)
        return b''.join([magic, command_name, payload_size, check_sum])

    def getblocks_message(self, header_hash):
        """
        Builds the getblocks payload, per the Bitcoin protocol.
        :param header_hash: locator block hash, for peer to find
        :return: getblocks message bytes
        """
        VERSION = 70015
        version = self.uint32_t(VERSION)
        hash_count = self.compactsize_t(1)
        # Assuming we pass in an already computed sha256(sha256(block)) hash
        block_header_hashes = bytes.fromhex(header_hash.hex())
        # Always ask for max number of blocks
        stop_hash = b'\0' * 32
        return b''.join([version, hash_count, block_header_hashes, stop_hash])

    def compactsize_t(self, n):
        """
        Marshals compactsize data type.
        :param n: integer
        :return: marshalled compactsize integer
        """
        if n < 252:
            return self.uint8_t(n)
        if n < 0xffff:
            return self.uint8_t(0xfd) + self.uint16_t(n)
        if n < 0xffffffff:
            return self.uint8_t(0xfe) + self.uint32_t(n)
        return self.uint8_t(0xff) + self.uint64_t(n)

    def uint8_t(self, n):
        """Marshal integer to unsigned, 8 bit"""
        return int(n).to_bytes(1, byteorder='little', signed=False)

    def uint16_t(self, n):
        """
        Returns an array of bytes representing the integer. The
        array of bytes is unsigned and the order is in little
        endian, the most significant byte is at the end.
        """
        return int(n).to_bytes(2, byteorder='little', signed=False)

    def uint32_t(self, n):
        """Marshal integer to unsigned, 32 bit"""
        return int(n).to_bytes(4, byteorder='little', signed=False)

    def uint64_t(self, n):
        """
        Returns an array of bytes representing the integer. The
        array of bytes is unsigned and the order is in little
        endian, the most significant byte is at the end.
        """
        return int(n).to_bytes(8, byteorder='little', signed=False)

    def print_message(self, msg, text=None, height=None):
        """
        Prints the contents of the bitcoin message
        :param msg: bitcoin message including header
        :return: message type
        """
        print('\n{}MESSAGE'.format('' if text is None else (text + ' ')))
        print('({}) {}'.format(len(msg), msg[:60].hex() + ('' if len(msg) < 60 else '...')))
        payload = msg[HEADER_SIZE:]
        command = self.print_header(msg[:HEADER_SIZE], checksum(payload))
        if command == 'version':
            self.print_version_msg(payload)
        elif command == 'sendcmpct':
            self.print_sendcmpct_message(payload)
        elif command == 'feefilter':
            self.print_feefilter_message(payload)
        elif command == 'addr':
            self.print_addr_message(payload)
        elif command == 'getblocks':
            self.print_getblocks_message(payload)
        elif command == 'inv' or command == 'getdata' or command == 'notfound':
            self.print_inv_message(payload, height)
        elif command == 'block':
            self.print_block_message(payload)
        return command

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

    def print_sendcmpct_message(self, payload):
        """
        Prints contents of the sendcmpct message.
        :param payload: sendcmpct message payload
        """
        announce, version = payload[:1], payload[1:]
        prefix = PREFIX * 2
        print('{}{:32} announce: {}'.format(prefix, announce.hex(), bytes(announce) != b'\0'))
        print('{}{:32} version: {}'.format(prefix, version.hex(), self.unmarshal_uint(version)))

    def print_feefilter_message(self, feerate):
        """
        Prints contents of the feefilter message.
        :param feerate: feefilter message payload
        """
        prefix = PREFIX * 2
        print('{}{:32} count: {}'.format(prefix, feerate.hex(), self.unmarshal_uint(feerate)))

    def print_addr_message(self, payload):
        """
        Prints contents of the addr message.
        :param payload: addr message payload
        """
        ip_count_bytes, ip_addr_count = self.unmarshal_compactsize(payload)
        i = len(ip_count_bytes)
        epoch_time, services, ip_addr, port = \
            payload[i:i + 4], payload[i + 4:i + 12], \
            payload[i + 12:i + 28], payload[i + 28:]
        prefix = PREFIX * 2
        print('{}{:32} count: {}'.format(prefix, ip_count_bytes.hex(), ip_addr_count))
        time_str = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(self.unmarshal_int(epoch_time)))
        print('{}{:32} epoch time: {}'.format(prefix, epoch_time.hex(), time_str))
        print('{}{:32} services: {}'.format(prefix, services.hex(), self.unmarshal_uint(services)))
        print('{}{:32} host: {}'.format(prefix, ip_addr.hex(), self.ipv6_to_ipv4(ip_addr)))
        print('{}{:32} port: {}'.format(prefix, port.hex(), self.unmarshal_uint(port)))

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

    def print_inv_message(self, payload, height):
        """
        Prints the contents of the inv message.
        :param payload: inv message payload
        :param height: local blockchain height
        """
        count_bytes, count = self.unmarshal_compactsize(payload)
        i = len(count_bytes)
        inventory = []
        for _ in range(count):
            inv_entry = payload[i: i + 4], payload[i + 4:i + 36]
            inventory.append(inv_entry)
            i += 36

        prefix = PREFIX * 2
        print('{}{:32} count: {}'.format(prefix, count_bytes.hex(), count))
        for i, (tx_type, tx_hash) in enumerate(inventory, start=height if height else 1):
            print('\n{}{:32} type: {}\n{}-'
                .format(prefix, tx_type.hex(), self.unmarshal_uint(tx_type), prefix))
            block_hash = self.swap_endian(tx_hash).hex()
            print('{}{:32}\n{}{:32} block #{} hash'.format(prefix, block_hash[:32], prefix, block_hash[32:], i))

    def print_getblocks_message(self, payload):
        """
        Prints contents of the getblocks message.
        :param payload: getblocks message payload
        """
        version = payload[:4]
        hash_count_bytes, hash_count = self.unmarshal_compactsize(payload[4:])
        i = 4 + len(hash_count_bytes)
        block_header_hashes = []
        for _ in range(hash_count):
            block_header_hashes.append(payload[i:i + 32])
            i += 32
        stop_hash = payload[i:]

        prefix = PREFIX * 2
        print('{}{:32} version: {}'.format(prefix, version.hex(), self.unmarshal_uint(version)))
        print('{}{:32} hash count: {}'.format(prefix, hash_count_bytes.hex(), hash_count))
        for hash in block_header_hashes:
            hash_hex = self.swap_endian(hash).hex()
            print('\n{}{:32}\n{}{:32} block header hash # {}: {}'
                .format(prefix, hash_hex[:32], prefix, hash_hex[32:], 1, self.unmarshal_uint(hash)))
        stop_hash_hex = stop_hash.hex()
        print('\n{}{:32}\n{}{:32} stop hash: {}'
            .format(prefix, stop_hash_hex[:32], prefix, stop_hash_hex[32:], self.unmarshal_uint(stop_hash)))

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
    """Converts an IPv4 address to IPv6."""
    pchIPv4 = bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xff, 0xff])
    return pchIPv4 + bytearray((int(x) for x in ipv4_str.split('.')))

def hash256(s):
    """Two rounds of sha256."""
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
    """Read_varint reads a variable integer from a stream."""
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
    """Turns a target integer back into bits, which is 4 bytes."""
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
    """Calculates the new bits given
    a 2016-block time differential and the previous bits"""
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
    """Takes the binary hashes and calculates the hash256"""
    # return the hash256 of hash1 + hash2
    return hash256(hash1 + hash2)

def merkle_parent_level(hashes):
    """Takes a list of binary hashes and returns a list that's half
    the length"""
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
    """Takes a list of binary hashes and returns the merkle root."""
    # current level starts as hashes
    current_level = hashes
    # loop until there's exactly 1 element
    while len(current_level) > 1:
        # current level becomes the merkle parent level
        current_level = merkle_parent_level(current_level)
    # return the 1st item of the current level
    return current_level[0]

def bits_to_target(bits):
    """Turns bits into a target (large 256-bit integer)."""
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
    DESTINATION_HOST = "89.234.180.194"
    # DESTINATION_HOST = "97.126.75.61"
    MY_BLOCK_NUMBER = "1085"

    node = Node(host=DESTINATION_HOST, block_number=MY_BLOCK_NUMBER, logging=True)
    node.handshake()
    node.lookup_block_number()
