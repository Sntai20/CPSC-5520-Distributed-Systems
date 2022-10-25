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

import selectors
import socket
import os
import fxp_bytes_subscriber

# Constants
CHECK_INTERVAL = 0.2  # seconds between checking for failure timeout
REQUEST_SIZE = 12

class MessagingServiceSubscriber():
    """
    Lab3 is used to subscribe to the Price Feed.
    """
    def __init__(self, listening_address, provider):
        """
        param: forex_provider_host localhost or 127.0.0.1
        param: forex_provider_port 50403
        forex_provider_address consists of forex_provider_host and forex_provider_port
        start a listening UDP server using localhost and port 50404
        """
        # Use the selector.
        self.selector = selectors.DefaultSelector()

        # Store the listening address and start the listening server.
        self.listening_address = listening_address
        self.incoming_messages_listener_socket = self.start_a_server(listening_address)

        # Store the Forex Provider socket info.
        self.provider = (socket.gethostbyname(provider[0]), int(provider[1]))
        self.provider_address, self.provider_port = self.provider[0], self.provider[1]

        # Subscribe to the publisher.
        # self.subscribe_to_a_publisher()

    # def run(self):
    #     """
    #     I think we need this to start the listening server and the subscriber.
    #     """
    #     self.start_a_server(("127.0.0.1", int("0")))
    #     self.subscribe_to_a_publisher()
    #     self.process_incoming_messages()

    def run(self):
        """
        Do the work of a group member as specified for Lab 2.
        """
        # print('STARTING WORK for pid {} on {}'.format(self.pid, self.listener_address))
        # self.join_group()
        self.selector.register(self.incoming_messages_listener_socket, selectors.EVENT_READ)
        # self.start_election('at startup')
        self.subscribe_to_a_publisher()
        while True:
            events = self.selector.select(CHECK_INTERVAL)
            for key, mask in events:
                if key.fileobj == self.incoming_messages_listener_socket:
                    # self.accept_peer()
                    self.process_incoming_messages(key.fileobj)
            #     elif mask & selectors.EVENT_READ:
            #         self.receive_message(key.fileobj)
                else:
                    self.process_incoming_messages(key.fileobj)
            # self.check_timeouts()

    def subscribe_to_a_publisher(self):
        """
        To subscribe to the price feed publisher, send your
        listening address to the forex provider.

        Start up a subscriber, use the subscriber_address
        to bind the socket to the publishers address.

        return: Print the messages received.
        """
        print(f"\nStarting subscriber, we receive messages on address {self.listening_address}")

        # Create a UDP socket and send the messages to current publisher.
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as subscriber:
            message = fxp_bytes_subscriber.serialize_address(self.listening_address)
            subscriber.sendto(message, self.provider)
            print(f"Sending a SUBSCRIBE request message {message} to the Forex Provider.")
            subscriber.close()

        # How do we handle renewing the subscription? The subscription expires every 10 minutes.

    @staticmethod
    def process_incoming_messages(incoming_message):
        """
        Process incoming messages using the listening address.
        """
        print(f"Listening for incoming messages from publisher. {incoming_message}")

        # try:
        # self.incoming_messages_listener_socket.accept()
        while True:
            print("\nblocking, waiting to receive message")
            incoming_message
            packet = incoming_message .incoming_messages_listener_socket.recv(4096)

            if not packet:
                raise ValueError('socket closed')
            data = packet

            print(f"received {len(data)} bytes")
            print(data)

    @staticmethod
    def start_a_server(listening_address):
        """
        Start up a listening server, use the LISTEN_PORT to bind
        the listening port and do not block the socket.

        return: A listener.
        """
        print(f"\nStarting LISTENER, we receive messages on address {listening_address}")
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as listener:
            listener.bind(listening_address)
            listener.setblocking(False)
            # return listener, listener.getsockname()
            return listener
            # incoming_messages = listener
            # print(f"Listening for incoming messages from the forex provider. {incoming_messages}")

            # while True:
            #     print("\nblocking, waiting to receive message")
            #     data = incoming_messages.recv(4096)

            #     print(f"received {len(data)} bytes")
            #     print(data)

if __name__ == '__main__':
    # Clearing the Screen
    os.system('clear')

    LISTEN_HOST = "127.0.0.1"
    # LISTEN_PORT = "50504"
    LISTEN_PORT = "0"
    LISTENING_ADDRESS = LISTEN_HOST, int(LISTEN_PORT)
    PROVIDER_ADDRESS = "127.0.0.1", int(50403)
    subscriber = MessagingServiceSubscriber(LISTENING_ADDRESS, PROVIDER_ADDRESS)
    # subscriber.process_incoming_messages()
    subscriber.run()
