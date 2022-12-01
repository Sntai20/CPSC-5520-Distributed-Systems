"""
STUDENT: Antonio Santana
FILE: lab5.py

DESCRIPTION:
    This program demonstrates lab5 takes a port number of
    an existing node and a key (any value from column 1+4 of the file).

USAGE:
    python3 lab5.py "Node_Port_Number" "Player_Id" "year"
    python3 lab5.py 12517 steveramsey/2523725 1970

"""
import hashlib
import os
# import ipaddress
# from time import gmtime, strftime
import time
import socket
from io import BytesIO
from random import randint

# class Lab5:
#     """Performs a query."""
#     def __init__(self, previous_block_hash, transaction_list):
#         """Placeholder."""
#         self.previous_block_hash = previous_block_hash
#         self.transaction_list = transaction_list

#         self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
#         self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
#         sent_version_message = VersionMessage()
#         sent_version_message.set_addr_recv_ip_address("127.0.0.1")
#         # version_message.set_version(70002)
#         b = sent_version_message.to_byte_array_string()
#         print(sent_version_message.print_version_msg(b))
#         sent_version_message.to_string()

# def send_message():
#     """
#     sending MESSAGE
#     (110) f9beb4d976657273696f6e0000000000560000003b9840b27f110100000000000000
#     00007833d25d0000000001000000000000000000000000000000...

#     HEADER
#     --------------------------------------------------------
#         f9beb4d9                         magic
#         76657273696f6e0000000000         command: version
#         56000000                         payload size: 86
#         3b9840b2                         checksum (verified)
#     VERSION
#     --------------------------------------------------------
#         7f110100                         version 70015
#         0000000000000000                 my services
#         7833d25d00000000                 epoch time Mon, 18 Nov 2019 06:00:24 GMT
#         0100000000000000                 your services
#         00000000000000000000ffff5c3fc0d1 your host 92.63.192.209
#         8d20                             your port 8333
#         0000000000000000                 my services (again)
#         00000000000000000000ffff0a000048 my host 10.0.0.72
#         9ee8                             my port 59550
#         0000000000000000                 nonce
#         00                               user agent size 0
#                                         user agent ''
#         00000000                         start height 0
#         00                               relay False
#     """

# def print_message(msg, text=None):
#     """
#     Report the contents of the given bitcoin message
#     :param msg: bitcoin message including header
#     :return: message type
#     """
#     print('\n{}MESSAGE'.format('' if text is None else (text + ' ')))
#     print('({}) {}'.format(len(msg), msg[:60].hex() + ('' if len(msg) < 60 else '...')))
#     payload = msg[HDR_SZ:]
#     command = print_header(msg[:HDR_SZ], checksum(payload))
#     if command == 'version':
#         print_version_msg(payload)
#     # FIXME print out the payloads of other types of messages, too
#     return command

# def print_version_msg(self, b):
#     """
#     Report the contents of the given bitcoin version message (sans the header)
#     :param payload: version message contents
#     """
#     # pull out fields
#     version, my_services, epoch_time, your_services = b[:4], b[4:12], b[12:20], b[20:28]
#     rec_host, rec_port, my_services2, my_host, my_port = b[28:44], b[44:46], b[46:54], b[54:70], b[70:72]
#     nonce = b[72:80]
#     user_agent_size, uasz = unmarshal_compactsize(b[80:])
#     i = 80 + len(user_agent_size)
#     user_agent = b[i:i + uasz]
#     i += uasz
#     start_height, relay = b[i:i + 4], b[i + 4:i + 5]
#     extra = b[i + 5:]

#     # print report
#     prefix = '  '
#     print(prefix + 'VERSION')
#     print(prefix + '-' * 56)
#     prefix *= 2
#     print('{}{:32} version {}'.format(prefix, version.hex(), unmarshal_int(version)))
#     print('{}{:32} my services'.format(prefix, my_services.hex()))
#     time_str = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime(unmarshal_int(epoch_time)))
#     print('{}{:32} epoch time {}'.format(prefix, epoch_time.hex(), time_str))
#     print('{}{:32} your services'.format(prefix, your_services.hex()))
#     print('{}{:32} your host {}'.format(prefix, rec_host.hex(), ipv6_to_ipv4(rec_host)))
#     print('{}{:32} your port {}'.format(prefix, rec_port.hex(), self.unmarshal_uint(rec_port)))
#     print('{}{:32} my services (again)'.format(prefix, my_services2.hex()))
#     print('{}{:32} my host {}'.format(prefix, my_host.hex(), ipv6_to_ipv4(my_host)))
#     print('{}{:32} my port {}'.format(prefix, my_port.hex(), self.unmarshal_uint(my_port)))
#     print('{}{:32} nonce'.format(prefix, nonce.hex()))
#     print('{}{:32} user agent size {}'.format(prefix, user_agent_size.hex(), uasz))
#     print('{}{:32} user agent \'{}\''.format(prefix, user_agent.hex(), str(user_agent, encoding='utf-8')))
#     print('{}{:32} start height {}'.format(prefix, start_height.hex(), self.unmarshal_uint(start_height)))
#     print('{}{:32} relay {}'.format(prefix, relay.hex(), bytes(relay) != b'\0'))
#     if len(extra) > 0:
#         print('{}{:32} EXTRA!!'.format(prefix, extra.hex()))

# def print_header(header, expected_cksum=None):
#     """
#     Report the contents of the given bitcoin message header
#     :param header: bitcoin message header (bytes or bytearray)
#     :param expected_cksum: the expected checksum for this version message, if known
#     :return: message type
#     """
#     magic, command_hex, payload_size, cksum = header[:4], header[4:16], header[16:20], header[20:]
#     command = str(bytearray([b for b in command_hex if b != 0]), encoding='utf-8')
#     psz = self.unmarshal_uint(payload_size)
#     if expected_cksum is None:
#         verified = ''
#     elif expected_cksum == cksum:
#         verified = '(verified)'
#     else:
#         verified = '(WRONG!! ' + expected_cksum.hex() + ')'
#     prefix = '  '
#     print(prefix + 'HEADER')
#     print(prefix + '-' * 56)
#     prefix *= 2
#     print('{}{:32} magic'.format(prefix, magic.hex()))
#     print('{}{:32} command: {}'.format(prefix, command_hex.hex(), command))
#     print('{}{:32} payload size: {}'.format(prefix, payload_size.hex(), psz))
#     print('{}{:32} checksum {}'.format(prefix, cksum.hex(), verified))
#     return command

# class BaseMessage():
    # """
    # Base Message container.
    # https://developer.bitcoin.org/reference/p2p_networking.html#version
    # The “version” message provides information about the transmitting node
    # to the receiving node at the beginning of a connection. Until both peers
    # have exchanged “version” messages, no other messages will be accepted.

    # If a “version” message is accepted, the receiving node should send a “verack”
    # message—but no node should send a “verack” message before initializing
    # its half of the connection by first sending a “version” message.
    # """
#     def __init__(self):
#         """
#         self._version = "4 int32_t required"
#         self.services = "8 unit64_t required"
#         self.timestamp = "8 unit64_t required"
#         self.addr_recv_services = "8 unit64_t required"
#         self.addr_recv_ip_address = "16 char[16] required"
#         self.addr_recv_port = "2 char[16] required"
#         self.addr_trans_services = "8 unit64_t required"
#         self.addr_trans_ip_address = "16 char[16] required"
#         self.addr_trans_port = "2 char[16] required"
#         self.nonce = "8 unit64_t required"
#         self.user_agent_bytes = "Varies compactSize uint required"
#         self.user_agent_string = "Required if user_agent bytes > 0"
#         self.start_height = "4 int32_t required"
#         self.relay = "1 bool optional"
#         """
#         self._version = bytearray(4)
#         self._services = bytearray(8)
#         self._timestamp = bytearray(8)
#         self._addr_recv_services = bytearray(8)
#         self._addr_recv_ip_address = bytearray(16)
#         self._addr_recv_port = bytearray(2)
#         self._addr_trans_services = bytearray(8)
#         self._addr_trans_ip_address = bytearray(16)
#         self._addr_trans_port = bytearray(2)
#         self._nonce = bytearray(8)
#         self._user_agent_bytes = bytearray(8)
#         self._user_agent_string = bytearray(8)
#         self._start_height = bytearray(4)
#         self._relay = bytearray(1)

#     def to_string(self):
#         """
#         Print version.
#         """
#         print(f"Version: {self.version()}")
#         print(f"Services: {self.services()}")
#         # print(f"timestamp: {self.timestamp()}")
#         print(f"addr_recv_services: {self.addr_recv_services()}")
#         print(f"addr_recv_ip_address: {self.addr_recv_ip_address()}")
#         print(f"addr_recv_port: {self.addr_recv_port()}")
#         print(f"addr_trans_services: {self.addr_trans_services()}")
#         print(f"addr_trans_ip_address: {self.addr_trans_ip_address()}")
#         print(f"addr_trans_port: {self.addr_trans_port()}")
#         print(f"nonce: {self.nonce()}")
#         print(f"user_agent_bytes: {self.user_agent_bytes()}")
#         print(f"user_agent_string: {self.user_agent_string()}")
#         print(f"start_height: {self.start_height()}")
#         print(f"relay: {self.relay()}")
#         """
#         Report the contents of the given bitcoin version message (sans the header)
#         :param payload: version message contents
#         """
#         # pull out fields
#         version, my_services, epoch_time, your_services = b[:4], b[4:12], b[12:20], b[20:28]
#         rec_host, rec_port, my_services2, my_host, my_port = b[28:44], b[44:46], b[46:54], b[54:70], b[70:72]
#         nonce = b[72:80]
#         user_agent_size, uasz = self.unmarshal_compactsize(b[80:])
#         i = 80 + len(user_agent_size)
#         user_agent = b[i:i + uasz]
#         i += uasz
#         start_height, relay = b[i:i + 4], b[i + 4:i + 5]
#         extra = b[i + 5:]

#         # print report
#         prefix = '  '
#         print(prefix + 'VERSION')
#         print(prefix + '-' * 56)
#         prefix *= 2
#         print('{}{:32} version {}'.format(prefix, version.hex(), self.unmarshal_int(version)))
#         print('{}{:32} version {}'.format(prefix, version.hex(), self.version()))
#         print('{}{:32} my services'.format(prefix, my_services.hex()))
#         time_str = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime(self.unmarshal_int(epoch_time)))
#         print('{}{:32} epoch time {}'.format(prefix, epoch_time.hex(), time_str))
#         print('{}{:32} your services'.format(prefix, your_services.hex()))
#         print('{}{:32} your host {}'.format(prefix, rec_host.hex(), self.ipv6_to_ipv4(rec_host)))
#         print('{}{:32} your port {}'.format(prefix, rec_port.hex(), self.unmarshal_uint(rec_port)))
#         print('{}{:32} my services (again)'.format(prefix, my_services2.hex()))
#         print('{}{:32} my host {}'.format(prefix, my_host.hex(), self.ipv6_to_ipv4(my_host)))
#         print('{}{:32} my port {}'.format(prefix, my_port.hex(), self.unmarshal_uint(my_port)))
#         print('{}{:32} nonce'.format(prefix, nonce.hex()))
#         print('{}{:32} user agent size {}'.format(prefix, user_agent_size.hex(), uasz))
#         print('{}{:32} user agent \'{}\''.format(prefix, user_agent.hex(), str(user_agent, encoding='utf-8')))
#         print('{}{:32} start height {}'.format(prefix, start_height.hex(), self.unmarshal_uint(start_height)))
#         print('{}{:32} relay {}'.format(prefix, relay.hex(), bytes(relay) != b'\0'))
#         if len(extra) > 0:
#             print('{}{:32} EXTRA!!'.format(prefix, extra.hex()))

#     def to_byte_array_string(self):
#         """
#         Print version.
#         """
#         message = self._version + self._services + self._timestamp + self._addr_recv_services + self._addr_recv_ip_address + self._addr_recv_port + self._addr_trans_services + self._addr_trans_ip_address + self._addr_trans_port + self._nonce + self._user_agent_bytes + self._user_agent_string + self._start_height + self._relay
#         return message

#     def version(self):
#         """
#         Returns the version in ascii.
#         """
#         number = self.unmarshal_int(self._version)
#         return number

#     def set_version(self, version):
#         """
#         Converts the version integer to an usigned array of bytes, then stores the array of bytes.
#         """
#         int_version = int(version)
#         self._version = self.uint8_t(int_version)

#     def services(self):
#         """
#         Returns the services in ascii.
#         """
#         return self.unmarshal_uint(self._services)

#     def set_services(self, services):
#         """
#         Converts the services integer to an array of bytes, then stores the array of bytes.
#         """
#         self._services = self.uint8_t(services)

#     def timestamp(self):
#         """
#         Returns the timestamp in ascii.
#         """
#         return self.unmarshal_uint(self._timestamp)

#     def set_timestamp(self, timestamp):
#         """
#         Converts the timestamp integer to an array of bytes, then stores the array of bytes.
#         """
#         self._timestamp = self.uint8_t(timestamp)

#     def addr_recv_services(self):
#         """
#         Returns the addr_recv_services in ascii.
#         """
#         return self.unmarshal_uint(self._addr_recv_services)

#     def set_addr_recv_services(self, addr_recv_services):
#         """
#         Converts the addr_recv_services integer to an array of bytes, then stores the array of bytes.
#         """
#         self._addr_recv_services = self.uint8_t(addr_recv_services)

#     def addr_trans_services(self):
#         """
#         Returns the addr_trans_services in ascii.
#         """
#         return self.unmarshal_uint(self._addr_trans_services)

#     def set_addr_trans_services(self, addr_trans_services):
#         """
#         Converts the addr_trans_services integer to an array of bytes, then stores the array of bytes.
#         """
#         self._addr_trans_services = self.uint8_t(addr_trans_services)

#     def nonce(self):
#         """
#         Returns the nonce in ascii.
#         """
#         return self.unmarshal_uint(self._nonce)

#     def set_nonce(self, nonce):
#         """
#         Converts the nonces integer to an array of bytes, then stores the array of bytes.
#         """
#         self._nonce = self.uint8_t(nonce)

#     def addr_recv_ip_address(self):
#         """
#         Returns the addr_recv_ip_address in ascii.
#         """
#         # return self.unmarshal_uint(self._addr_recv_ip_address)
#         return ipaddress.IPv4Address(self._addr_recv_ip_address)

#     def set_addr_recv_ip_address(self, addr_recv_ip_address):
#         """
#         Converts the addr_recv_ip_address integer to an array of
#         bytes, then stores the array of bytes.
#         """
#         receive_ip_in_bytes = ipaddress.IPv4Address(addr_recv_ip_address).packed
#         # my_bytes = self.uint16_t(addr_recv_ip_address)
#         self._addr_recv_ip_address = receive_ip_in_bytes

#     def addr_trans_ip_address(self):
#         """
#         Returns the addr_trans_ip_address in ascii.
#         """
#         return self.unmarshal_uint(self._addr_trans_ip_address)

#     def set_addr_trans_ip_address(self, addr_trans_ip_address):
#         """
#         Converts the addr_trans_ip_address integer to an array
#         of bytes, then stores the array of bytes.
#         """
#         self._addr_trans_ip_address = self.uint16_t(addr_trans_ip_address)

#     def addr_recv_port(self):
#         """
#         Returns the addr_recv_port in ascii.
#         """
#         return self.unmarshal_uint(self._addr_recv_port)

#     def set_addr_recv_port(self, addr_recv_port):
#         """
#         Converts the addr_recv_port integer to an array of bytes, then stores the array of bytes.
#         """
#         self._addr_recv_port = self.uint8_t(addr_recv_port)

#     def addr_trans_port(self):
#         """
#         Returns the addr_trans_port in ascii.
#         """
#         return self.unmarshal_uint(self._addr_trans_port)

#     def set_addr_trans_port(self, addr_trans_port):
#         """
#         Converts the addr_trans_port integer to an array of bytes, then stores the array of bytes.
#         """
#         self._addr_trans_port = self.uint8_t(addr_trans_port)

#     def start_height(self):
#         """
#         Returns the start_height in ascii.
#         """
#         return self.unmarshal_uint(self._start_height)

#     def set_start_height(self, start_height):
#         """
#         Converts the start_height integer to an array of bytes, then stores the array of bytes.
#         """
#         self._start_height = self.uint8_t(start_height)

#     def relay(self):
#         """
#         Returns the relay in ascii.
#         """
#         return self.unmarshal_uint(self._relay)

#     def set_relay(self, relay):
#         """
#         Converts the relay integer to an array of bytes, then stores the array of bytes.
#         """
#         self._relay = self.uint8_t(relay)

#     def user_agent_bytes(self):
#         """
#         Returns the user_agent_bytes in ascii.
#         """
#         return self.unmarshal_uint(self._user_agent_bytes)

#     def set_user_agent_bytes(self, user_agent_bytes):
#         """
#         Converts the user_agent_bytes integer to an array of bytes, then stores the array of bytes.
#         """
#         self._user_agent_bytes = self.uint8_t(user_agent_bytes)

#     def user_agent_string(self):
#         """
#         Returns the user_agent_string in ascii.
#         """
#         return self.unmarshal_uint(self._user_agent_string)

#     def set_user_agent_string(self, user_agent_string):
#         """
#         Converts the user_agent_string integer to an array of bytes, then stores the array of bytes.
#         """
#         # TODO Make sure we are using appropriate size.
#         self._user_agent_string = self.uint8_t(user_agent_string)

#     # def replaceme(self):
#     #     """
#     #     Returns the replaceme in ascii.
#     #     """
#     #     return self.replaceme

#     # def set_replaceme(self, replaceme):
#     #     """
#     #     Converts the replaceme integer to an array of bytes, then stores the array of bytes.
#     #     """
#     #     self.replaceme = self.uint8_t(replaceme)

#     def compactsize_t(self, n):
#         """
#         placeholder
#         """
#         if n < 252:
#             return self.uint8_t(n)
#         if n < 0xffff:
#             return self.uint8_t(0xfd) + self.uint16_t(n)
#         if n < 0xffffffff:
#             return self.uint8_t(0xfe) + self.uint32_t(n)
#         return self.uint8_t(0xff) + self.uint64_t(n)

#     def unmarshal_compactsize(self, b):
#         """
#         placeholder
#         """
#         key = b[0]
#         if key == 0xff:
#             return b[0:9], self.unmarshal_uint(b[1:9])
#         if key == 0xfe:
#             return b[0:5], self.unmarshal_uint(b[1:5])
#         if key == 0xfd:
#             return b[0:3], self.unmarshal_uint(b[1:3])
#         return b[0:1], self.unmarshal_uint(b[0:1])

#     def bool_t(self, flag):
#         """
#         Returns an 8-bit unsigned integer of the boolean.
#         """
#         return self.uint8_t(1 if flag else 0)

#     def ipv6_from_ipv4(self, ipv4_str):
#         """
#         Converts an IPv4 address to IPv6.
#         """
#         pchIPv4 = bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xff, 0xff])
#         return pchIPv4 + bytearray((int(x) for x in ipv4_str.split('.')))

#     def ipv6_to_ipv4(self, ipv6):
#         """
#         Converts an IPv6 address to IPv4.
#         """
#         return '.'.join([str(b) for b in ipv6[12:]])

#     def uint8_t(self, n):
#         """
#         Returns an array of bytes representing the integer. The
#         array of bytes is unsigned and the order is in little
#         endian, the most significant byte is at the end.
#         """
#         return int(n).to_bytes(1, byteorder='little', signed=False)

#     def uint16_t(self, n):
#         """
#         Returns an array of bytes representing the integer. The
#         array of bytes is unsigned and the order is in little
#         endian, the most significant byte is at the end.
#         """
#         return int(n).to_bytes(2, byteorder='little', signed=False)

#     def int32_t(self, n):
#         """
#         Returns an array of bytes representing the integer. The 
#         array of bytes is signed and the order is in little endian,
#         the most significant byte is at the end.
#         """
#         return int(n).to_bytes(4, byteorder='little', signed=True)

#     def uint32_t(self, n):
#         """
#         Returns an array of bytes representing the integer. The
#         array of bytes is unsigned and the order is in little
#         endian, the most significant byte is at the end.
#         """
#         return int(n).to_bytes(4, byteorder='little', signed=False)

#     def int64_t(self, n):
#         """
#         Returns an array of bytes representing the integer. The 
#         array of bytes is signed and the order is in little endian,
#         the most significant byte is at the end.
#         """
#         return int(n).to_bytes(8, byteorder='little', signed=True)

#     def uint64_t(self, n):
#         """
#         Returns an array of bytes representing the integer. The
#         array of bytes is unsigned and the order is in little
#         endian, the most significant byte is at the end.
#         """
#         return int(n).to_bytes(8, byteorder='little', signed=False)

#     def unmarshal_int(self, b):
#         """
#         Returns the integer version of the byte array. The byte array
#         is signed and the order is in little endian, the most
#         significant byte is at the end.
#         """
#         return int.from_bytes(b, byteorder='little', signed=True)

#     def unmarshal_uint(self, b):
#         """
#         Returns the integer version of an array of bytes. The byte array
#         is unsigned and the order is in little endian, the most
#         significant byte is at the end.
#         """
#         return int.from_bytes(b, byteorder='little', signed=False)

# class VersionMessage(BaseMessage):
#     """
#     Version Message container.
#     https://developer.bitcoin.org/reference/p2p_networking.html#version
#     The “version” message provides information about the transmitting node
#     to the receiving node at the beginning of a connection. Until both peers
#     have exchanged “version” messages, no other messages will be accepted.

#     If a “version” message is accepted, the receiving node should send a “verack”
#     message—but no node should send a “verack” message before initializing
#     its half of the connection by first sending a “version” message.
#         self._version = "4 int32_t required"
#         self.services = "8 unit64_t required"
#         self.timestamp = "8 unit64_t required"
#         self.addr_recv_services = "8 unit64_t required"
#         self.addr_recv_ip_address = "16 char[16] required"
#         self.addr_recv_port = "2 char[16] required"
#         self.addr_trans_services = "8 unit64_t required"
#         self.addr_trans_ip_address = "16 char[16] required"
#         self.addr_trans_port = "2 char[16] required"
#         self.nonce = "8 unit64_t required"
#         self.user_agent_bytes = "Varies compactSize uint required"
#         self.user_agent_string = "Required if user_agent bytes > 0"
#         self.start_height = "4 int32_t required"
#         self.relay = "1 bool optional"
#     """
#     def to_string(self):
#         """
#         Print version.
#         """
#         print(f"Version: {self.version()}")
#         print(f"Services: {self.services()}")
#         print(f"timestamp: {self.timestamp()}")
#         print(f"addr_recv_services: {self.addr_recv_services()}")
#         print(f"addr_recv_ip_address: {self.addr_recv_ip_address()}")
#         print(f"addr_recv_port: {self.addr_recv_port()}")
#         print(f"addr_trans_services: {self.addr_trans_services()}")
#         print(f"addr_trans_ip_address: {self.addr_trans_ip_address()}")
#         print(f"addr_trans_port: {self.addr_trans_port()}")
#         print(f"nonce: {self.nonce()}")
#         print(f"user_agent_bytes: {self.user_agent_bytes()}")
#         print(f"user_agent_string: {self.user_agent_string()}")
#         print(f"start_height: {self.start_height()}")
#         print(f"relay: {self.relay()}")

#     def print_version_msg(self, b):
#         """
#         Report the contents of the given bitcoin version message (sans the header)
#         :param payload: version message contents
#         """
#         # pull out fields
#         version, my_services, epoch_time, your_services = b[:4], b[4:12], b[12:20], b[20:28]
#         rec_host, rec_port, my_services2, my_host, my_port = b[28:44], b[44:46], b[46:54], b[54:70], b[70:72]
#         nonce = b[72:80]
#         user_agent_size, uasz = self.unmarshal_compactsize(b[80:])
#         i = 80 + len(user_agent_size)
#         user_agent = b[i:i + uasz]
#         i += uasz
#         start_height, relay = b[i:i + 4], b[i + 4:i + 5]
#         extra = b[i + 5:]

#         # print report
#         prefix = '  '
#         print(prefix + 'VERSION')
#         print(prefix + '-' * 56)
#         prefix *= 2
#         print('{}{:32} version {}'.format(prefix, version.hex(), self.unmarshal_int(version)))
#         print('{}{:32} version {}'.format(prefix, version.hex(), self.version()))
#         print('{}{:32} my services'.format(prefix, my_services.hex()))
#         time_str = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime(self.unmarshal_int(epoch_time)))
#         print('{}{:32} epoch time {}'.format(prefix, epoch_time.hex(), time_str))
#         print('{}{:32} your services'.format(prefix, your_services.hex()))
#         print('{}{:32} your host {}'.format(prefix, rec_host.hex(), self.ipv6_to_ipv4(rec_host)))
#         print('{}{:32} your port {}'.format(prefix, rec_port.hex(), self.unmarshal_uint(rec_port)))
#         print('{}{:32} my services (again)'.format(prefix, my_services2.hex()))
#         print('{}{:32} my host {}'.format(prefix, my_host.hex(), self.ipv6_to_ipv4(my_host)))
#         print('{}{:32} my port {}'.format(prefix, my_port.hex(), self.unmarshal_uint(my_port)))
#         print('{}{:32} nonce'.format(prefix, nonce.hex()))
#         print('{}{:32} user agent size {}'.format(prefix, user_agent_size.hex(), uasz))
#         print('{}{:32} user agent \'{}\''.format(prefix, user_agent.hex(), str(user_agent, encoding='utf-8')))
#         print('{}{:32} start height {}'.format(prefix, start_height.hex(), self.unmarshal_uint(start_height)))
#         print('{}{:32} relay {}'.format(prefix, relay.hex(), bytes(relay) != b'\0'))
#         if len(extra) > 0:
#             print('{}{:32} EXTRA!!'.format(prefix, extra.hex()))

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
        result += b'\x00' * 10 + b'\xff\xff' + self.receiver_ip
        # receiver port is 2 bytes, big endian
        result += self.receiver_port.to_bytes(2, 'big')
        # sender services is 8 bytes little endian
        result += int_to_little_endian(self.sender_services, 8)
        # IPV4 is 10 00 bytes and 2 ff bytes then sender ip
        result += b'\x00' * 10 + b'\xff\xff' + self.sender_ip
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
        return cls()

    def serialize(self):
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
    TODO: Which version are we using? 70015 is the latest verion.
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
        """
        Appends the data.
        """
        self.data.append((data_type, identifier))

    def serialize(self):
        """
        start with the number of items as a varint
        """
        result = encode_varint(len(self.data))
        # loop through each tuple (data_type, identifier) in self.data
        for data_type, identifier in self.data:
            # data type is 4 bytes Little-Endian
            result += int_to_little_endian(data_type, 4)
            # identifier needs to be in Little-Endian
            result += identifier[::-1]
        return result

class GenericMessage:
    """
    Generic Message.
    """
    def __init__(self, command, payload):
        self.command = command
        self.payload = payload

    def serialize(self):
        return self.payload

TX_DATA_TYPE = 1
BLOCK_DATA_TYPE = 2
FILTERED_BLOCK_DATA_TYPE = 3
COMPACT_BLOCK_DATA_TYPE = 4

NETWORK_MAGIC = b'\xf9\xbe\xb4\xd9'
TESTNET_NETWORK_MAGIC = b'\x0b\x11\x09\x07'

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

    def handshake(self):
        """
        Do a handshake with the other node.Handshake is sending
        a version message and getting a verack back.
        create a version message
        send the command
        wait for a verack message
        """
        version = VersionMessage()
        if self.logging:
            print(f"Handshake with host {host} on the main network.")
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
            print(f'sending: {envelope}')
            # print(self.print_version_msg(envelope))
        self.socket.sendall(envelope.serialize())
        # print(f"Sending Version message in the envelope {envelope}")

    def read(self):
        """
        Read a message from the socket.
        """
        envelope = NetworkEnvelope.parse(self.stream, testnet=self.testnet)
        if self.logging:
            print(f'receiving: {envelope}')
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
            elif command == PingMessage.command:
                # send pong
                self.send(PongMessage(envelope.payload))
        return command_to_class[command].parse(envelope.stream())

    # def print_version_msg(self, b):
    #     """
    #     Report the contents of the given bitcoin version message (sans the header)
    #     :param payload: version message contents
    #     """
    #     # pull out fields
    #     version, my_services, epoch_time, your_services = b[:4], b[4:12], b[12:20], b[20:28]
    #     rec_host, rec_port, my_services2, my_host, my_port = b[28:44], b[44:46], b[46:54], b[54:70], b[70:72]
    #     nonce = b[72:80]
    #     user_agent_size, uasz = unmarshal_compactsize(b[80:])
    #     i = 80 + len(user_agent_size)
    #     user_agent = b[i:i + uasz]
    #     i += uasz
    #     start_height, relay = b[i:i + 4], b[i + 4:i + 5]
    #     extra = b[i + 5:]

    #     # print report
    #     prefix = '  '
    #     print(prefix + 'VERSION')
    #     print(prefix + '-' * 56)
    #     prefix *= 2
    #     print('{}{:32} version {}'.format(prefix, version.hex(), little_endian_to_int(version)))
    #     print('{}{:32} my services'.format(prefix, my_services.hex()))
    #     time_str = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime(little_endian_to_int(epoch_time)))
    #     print('{}{:32} epoch time {}'.format(prefix, epoch_time.hex(), time_str))
    #     print('{}{:32} your services'.format(prefix, your_services.hex()))
    #     print('{}{:32} your host {}'.format(prefix, rec_host.hex(), ipv6_to_ipv4(rec_host)))
    #     print('{}{:32} your port {}'.format(prefix, rec_port.hex(), self.unmarshal_uint(rec_port)))
    #     print('{}{:32} my services (again)'.format(prefix, my_services2.hex()))
    #     print('{}{:32} my host {}'.format(prefix, my_host.hex(), ipv6_to_ipv4(my_host)))
    #     print('{}{:32} my port {}'.format(prefix, my_port.hex(), self.unmarshal_uint(my_port)))
    #     print('{}{:32} nonce'.format(prefix, nonce.hex()))
    #     print('{}{:32} user agent size {}'.format(prefix, user_agent_size.hex(), uasz))
    #     print('{}{:32} user agent \'{}\''.format(prefix, user_agent.hex(), str(user_agent, encoding='utf-8')))
    #     print('{}{:32} start height {}'.format(prefix, start_height.hex(), self.unmarshal_uint(start_height)))
    #     print('{}{:32} relay {}'.format(prefix, relay.hex(), bytes(relay) != b'\0'))
    #     if len(extra) > 0:
    #         print('{}{:32} EXTRA!!'.format(prefix, extra.hex()))

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

    def ipv6_from_ipv4(self, ipv4_str):
        """
        Converts an IPv4 address to IPv6.
        """
        pchIPv4 = bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xff, 0xff])
        return pchIPv4 + bytearray((int(x) for x in ipv4_str.split('.')))

    def ipv6_to_ipv4(self, ipv6):
        """
        Converts an IPv6 address to IPv4.
        """
        return '.'.join([str(b) for b in ipv6[12:]])

# Helpers
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

if __name__ == '__main__':
    # 97.126.42.129:8333
    # 97-126-42-129.tukw.qwest.net
    # host = '97-126-42-129.tukw.qwest.net'
    host = '89.234.180.194'

    print("Clearing the Screen")
    os.system('clear')

    print(f"Create node, enable logging, and attempt to handshake with host {host} on the main network.")
    node = Node(host=host, logging=True)
    node.handshake()
