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

import os
import socket
import threading
import time
import fxp_bytes_subscriber

class MessagingServiceSubscriber:
    """
    Lab3 is used to subscribe to the Price Feed.
    """

    @staticmethod
    def subscriber_client():
        """
        To subscribe to the simple publisher.

        return: Print the messages received.
        """
        server_address = ('localhost', 10000)
        print(f"Starting up on address {server_address}")

        # Create a UDP socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind(server_address)  # subscriber binds the socket to the publishers address
            while True:
                print('\nblocking, waiting to receive message')
                data = sock.recv(4096)

                print(f"Received {len(data)} bytes")
                print(data)
                time.sleep(1.0)

    @staticmethod
    def start_a_server():
        """
        Start up a listening server, use the LISTEN_PORT to bind
        the listening port and do not block the socket.

        return: A listener.
        """
        # listening_address = ("127.0.0.1", int("50504"))
        server_address = ('localhost', 20000)
        print("\nStarting LISTENER, we receive messages on address 127.0.0.1, 20000")
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as listener:
            listener.bind(server_address)
            # listener.setblocking(True)
            # return listener, listener.getsockname()
            # return listener
            # incoming_messages = listener
            # print(f"Listening for incoming messages from the forex provider. {incoming_messages}")

            while True:
                # print("\nblocking, waiting to receive message")
                incoming_data = listener.recv(4096)

                # print(f"received {len(incoming_data)} bytes")
                # print(incoming_data)

                # Parse the individual quotes from the message.
                """
                Unmarshall the message [
                {'timestamp': datetime.datetime(2022, 10, 25, 20, 17, 48, 438084),
                'cross': 'GBP/USD', 'price': 1.25052},
                {'timestamp': datetime.datetime(2022, 10, 25, 20, 17, 48, 438084),
                'cross': 'EUR/USD', 'price': 1.10254},
                {'timestamp': datetime.datetime(2022, 10, 25, 20, 17, 48, 438084),
                'cross': 'USD/JPY', 'price': 99.92674},
                {'timestamp': datetime.datetime(2022, 10, 25, 20, 17, 48, 438084),
                'cross': 'AUD/USD', 'price': 0.74889},
                {'timestamp': datetime.datetime(2022, 10, 25, 20, 17, 48, 438084),
                'cross': 'USD/CHF', 'price': 1.00142},
                {'timestamp': datetime.datetime(2022, 10, 25, 20, 17, 48, 438084),
                'cross': 'CAD/CHF', 'price': 49.67480855959658},
                {'timestamp': datetime.datetime(2022, 10, 25, 20, 17, 48, 438084),
                'cross': 'CAD/JPY', 'price': 198.6992342383863}
                ] from the Forex Provider.
                """
                messages = fxp_bytes_subscriber.unmarshall_message(incoming_data)

                # print(f"Unmarshall the messages {messages} from the Forex Provider.")
                # handle each quote in the quote list (list of dicts, ea dict is a quote)
                # 2019-10-14 23:58:36.216488 EUR USD 1.1005
                for message in messages:
                    # print(message)
                    print(f"{message['timestamp']} {message['cross']} {message['price']}")

    @staticmethod
    def subscribe_to_a_publisher():
        """
        To subscribe to the price feed publisher, send your
        listening address to the forex provider.

        Start up a subscriber, use the subscriber_address
        to bind the socket to the publishers address.

        return: Print the messages received.
        """
        while True:
            # Create a UDP socket and send the messages to the publisher.
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as subscriber:
                server_address = ("127.0.0.1", 20000)
                message = fxp_bytes_subscriber.serialize_address(server_address)

                subscriber.sendto(message, ("127.0.0.1", 50403))
                print(f"Sending a SUBSCRIBE request message {message} to the Forex Provider.")
                subscriber.close()

            # How do we handle renewing the subscription? The subscription expires every 10 minutes.
            time.sleep(5.0)

if __name__ == '__main__':
    # Clearing the Screen
    os.system('clear')

    # Use one thread to send a subscribe request
    # and a seperate thread to process incomming messages.
    start_a_server_thread = threading.Thread(target=MessagingServiceSubscriber.start_a_server)
    start_a_server_thread.start()
    subscribe_thread = threading.Thread(target=MessagingServiceSubscriber.subscribe_to_a_publisher)
    subscribe_thread.start()

    # Simple Pub/Sub test.
    # subscriber_client_thread = threading.Thread(target=MessagingServiceSubscriber.subscriber_client)
    # subscriber_client_thread.start()
