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
import os
import fxp_bytes_subscriber

# Constants
REQUEST_SIZE = 12

class MessagingServiceSubscriber():
    """
    Lab3 is used to subscribe to the Price Feed.
    """
    def __init__(self, listening_address):
        """
        param: forex_provider_host localhost or 127.0.0.1
        param: forex_provider_port 50403
        forex_provider_address consists of forex_provider_host and forex_provider_port
        start a listening UDP server using localhost and port 50404
        """
        # self.listener, self.listener_address = self.start_a_server(listening_address)
        self.listening_address = listening_address
        self.incoming_messages = self.start_a_server(listening_address)
        # self.subscribe_to_a_publisher()

    def subscribe_to_a_publisher(self, subscriber_address):
        """
        To subscribe to the price feed publisher, send your
        listening address to the forex provider.
        
        Start up a subscriber, use the subscriber_address
        to bind the socket to the publishers address.

        return: Print the messages received.
        """
        # server_address = (subscriber_address)
        print(f"\nStarting subscriber up on {subscriber_address[0]} port {subscriber_address[1]}")

        # Create a UDP socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind(subscriber_address)  # subscriber binds the socket to the publishers address
            sock.setblocking(False)
            
            # send the messages to current publisher.
            # self.subscribe_to_a_publisher()
            data = self.listening_address
            print(f"Subscribe to the price feed, we will receive messages on address {self.listening_address}")
            message = fxp_bytes_subscriber.serialize_address(data)
            # marshal_message(data)
            print(f"Sending a SUBSCRIBE request message {message} to the Forex Provider.")
            # sock.send(message)

            # while True:
            #     print("\nblocking, waiting to receive message")
            #     data = sock.recv(4096)

            #     print(f"received {len(data)} bytes")
            #     print(data)

    # def subscribe_to_a_publisher(self):
    #     """
        # To subscribe to the price feed publisher, send your
        # listening address to the forex provider.
    #     """
    #     data = self.listening_address
    #     print(f"Subscribe to the price feed, we will receive messages on address {self.listening_address}")
    #     fxp_bytes_subscriber.marshal_message(data)
    
    def process_incoming_messages(self):
        print(f"Listening for incoming messages from the forex provider. {self.incoming_messages}")
        
        while True:
            print("\nblocking, waiting to receive message")
            data = self.incoming_messages.recv(4096)

            print(f"received {len(data)} bytes")
            print(data)

    @staticmethod
    def start_a_server(listening_address):
        """
        Start up a listening server, use the LISTEN_PORT to bind
        the listening port and do not block the socket.

        return: A listener.
        """
        listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        listener.bind(listening_address)
        listener.setblocking(False)
        # return listener, listener.getsockname()
        return listener

if __name__ == '__main__':
    # Clearing the Screen
    os.system('clear')

    LISTEN_HOST = "127.0.0.1"
    LISTEN_PORT = "50504"
    LISTENING_ADDRESS = LISTEN_HOST, int(LISTEN_PORT)
    SUBSCRIBER_ADDRESS = "127.0.0.1", int(50405)
    subscriber = MessagingServiceSubscriber(LISTENING_ADDRESS)
    subscriber.subscribe_to_a_publisher(SUBSCRIBER_ADDRESS)
