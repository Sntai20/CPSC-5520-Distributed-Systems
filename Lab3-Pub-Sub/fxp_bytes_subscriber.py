"""
Forex Subscriber
This module contains useful marshalling functions for manipulating 
Forex Provider packet contents.
"""

# from array import array
import socket

def serialize_address(subscriber_listening_address: tuple) -> bytes:
    """
    Convert the host, port address to a 6-byte sequence of bytes (a byte array).
    :param subscriber_listening_address: data to be converted.
    :return: bytes
    """
    host_ip_in_bytes = socket.inet_aton(subscriber_listening_address[0])
    print(f"Convert this host {subscriber_listening_address[0]} to bytes {host_ip_in_bytes}")

    port_in_bytes = socket.inet_aton(str(subscriber_listening_address[1]))[2:]
    print(f"Convert this port {subscriber_listening_address[1]} to bytes {port_in_bytes}")

    # An array of 6-bytes.
    message = host_ip_in_bytes + port_in_bytes

    return message

def marshal_message(data_sequence) -> bytes:
    """
    Construct the byte stream for a message given a data_sequence.
    return: byte stream to send in a UDP message.
    """
    print(f"Hello Lab3. data_sequence {data_sequence}")
    message = data_sequence
    return message
