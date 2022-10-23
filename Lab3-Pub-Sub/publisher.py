"""
FILE: lab3.py

DESCRIPTION:
    This program demonstrates common scenarios like instantiating a client,
    creating a queue, and sending and receiving messages.

USAGE:
    python3 lab3.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_STORAGE_CONNECTION_STRING - the connection string to your storage account
"""
import socket
import time

class MessagingServicePublisher():
    """Simple Messaging Service class used to send and receive messages to an Queue."""
    def create_publish_client(self):
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(sock)

        server_address = ('localhost', 10000)
        for n in range(10_000):
            message = 'message {}'.format(n).encode('utf-8')
            print('sending {!r} (even if nobody is listening)'.format(message))
            sent = sock.sendto(message, server_address)  # the publisher does not do a bind
            print(sock)
            time.sleep(1.0)

if __name__ == '__main__':
    publisher = MessagingServicePublisher()
    publisher.create_publish_client()
