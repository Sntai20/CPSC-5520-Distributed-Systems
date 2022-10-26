"""
Forex Subscriber
This module contains useful marshalling functions for manipulating
Forex Provider packet contents.
"""

from array import array
# from datetime import datetime
import datetime
import socket

def serialize_address(subscriber_listening_address: tuple) -> bytes:
    """
    Convert the host, port address to a 6-byte sequence of bytes (a byte array).
    :param subscriber_listening_address: data to be converted.
    :return: bytes
    """
    host_ip_in_bytes = socket.inet_aton(subscriber_listening_address[0])
    # print(f"Convert this host {subscriber_listening_address[0]} to bytes {host_ip_in_bytes}")

    port_in_bytes = socket.inet_aton(str(subscriber_listening_address[1]))[2:]
    # print(f"Convert this port {subscriber_listening_address[1]} to bytes {port_in_bytes}")

    # An array of 6-bytes.
    message = host_ip_in_bytes + port_in_bytes

    return message

def deserialize_cross(b: bytes) -> str:
    """
    Converts 8-bit ASCII characers to strings.
    :param b:byte array
    :return: fromated string eg 'GBP/USD'
    """
    s = b.decode()
    return s[0:3] + '/' + s[3:]

def deserialize_datetime(b: bytes) -> datetime:
    """
    Convert an 8 byte big-endian byte array to a microseconds. Switches from big to
    little endian. Datetime object in byte array represents a UTC timestamp for a
    corresponding provider message.
    Reference: https://www.geeksforgeeks.org/convert-python-datetime-to-epoch

    :param b: byte array
    :return: datetime in microsecs
    """

    micros_per_seconds = 1e+6

    microseconds = int.from_bytes(b, byteorder='big')
    epoch_time = datetime.datetime(1970, 1, 1, 0, 0, 0, 0)
    date_time = (epoch_time + datetime.timedelta(seconds=microseconds / micros_per_seconds))

    # print(f"{date_time} Parse the datetime.")
    return date_time

def deserialize_price(price_in_bytes: bytes) -> float:
    """
    Convert a byte array representing a price to float.
    :param b: 8-byte array of floating point numbers
    :return: float representation of b
    """

    # Initialize an array, of type 'd' float.
    price = array('d')
    price.frombytes(price_in_bytes)

    # print(f"{price[0]} Convert and store the price_in_bytes into the price array as a float value.")
    return price[0]

def unmarshall_message(b: bytes) -> list:
    """
    Unmarshall a byte message into a formated list of dicts representing Forex quotes.
    :param b: 32b array message from Forex provider in the following format
    <timestamp, currency 1, currency 2, exchange rate>
    b[0:8]   - timestamp, 64b int num of microseconds in UTC, big endian
    b[8:14]  - currency names as ISO codes 'USD, 'GDP' in 8b ASCII from left to right
    b[14:22] - exchange rate as a 64b float in little endian
    b[22:32] - reserved, not used, set to x00
    :returns: a list of dicts representing Forex quotes
    """
    # Unmarshall Message Constants
    TIMESTAMP, CROSS, PRICE = 'timestamp', 'cross', 'price'
    # per spec, each quote is no more than 32 bytes
    MESSAGE_SIZE = 32
    # holds unmarshalled list of dictionaries representing quotes
    quote_list = []
    # calculate the total number of quotes contained in the UDP byte array
    total_message_size = len(b)
    n_quotes = int(total_message_size / MESSAGE_SIZE)

    # populate quotes into list of dicts
    for i in range(n_quotes):
        quote = {}

        # get the bytes the next quote in the list
        start_quote = i * MESSAGE_SIZE
        end_quote = start_quote + MESSAGE_SIZE
        b_quote = b[start_quote:end_quote]

        b_time, b_cross, b_price = b_quote[0:8], b_quote[8:14], b_quote[14:22]

        quote[TIMESTAMP] = deserialize_datetime(b_time)
        quote[CROSS] = deserialize_cross(b_cross)
        quote[PRICE] = deserialize_price(b_price)

        quote_list.append(quote)

    return quote_list

def marshal_message(data_sequence) -> bytes:
    """
    Construct the byte stream for a message given a data_sequence.
    return: byte stream to send in a UDP message.
    """
    print(f"Hello Lab3. data_sequence {data_sequence}")
    message = data_sequence
    return message
