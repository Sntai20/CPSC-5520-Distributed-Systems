"""
Forex Subscriber
This module contains useful marshalling functions for manipulating 
Forex Provider packet contents.
"""

from array import array

def serialize_address(subscriber_listening_address) -> bytes:
    """
    Convert the host, port address to a 6-byte sequence of bytes.
    :param subscriber_listening_address: data to be converted.
    :return: bytes
    """
    print(f"Convert this host {subscriber_listening_address[0]} port {subscriber_listening_address[1]} to an array of 6-bytes")
    # subscriber_listening_address[0]
    print(f"Convert this host {subscriber_listening_address[0]} to bytes")
    port = subscriber_listening_address[1]
    port_array = array('H', [int(port)])
    # port_array.byteswap() # to little-endian
    # port_array.tobytes()
    # port_array.fromunicode(str(port))
    print(f"Convert this port {subscriber_listening_address[1]} to {port_array.byteswap()} bytes {port_array.tobytes()}")
    message = subscriber_listening_address
    return message

def marshal_message(data_sequence) -> bytes:
    """
    Construct the byte stream for a message given a data_sequence.
    return: byte stream to send in a UDP message.
    """
    print(f"Hello Lab3. data_sequence {data_sequence}")
    message = data_sequence
    return message
