"""
STUDENT: Antonio Santana
FILE: lab3.py

DESCRIPTION:
    This program demonstrates common scenarios like instantiating a client,
    creating a queue, and sending and receiving messages.

USAGE:
    python3 lab3.py

"""

import math
import os
import socket
import threading
import time
import bellman_ford
import fxp_bytes_subscriber

class MessagingServiceSubscriber:
    """
    Lab3 is used to subscribe to the Price Feed.
    """
    def __init__(self):
        """Constructor"""
        # self.graph = {}
        # self.add_to_graph(self)

    @staticmethod
    def start_a_server():
        """
        Start up a listening server, use the LISTEN_PORT to bind
        the listening port and do not block the socket.

        return: A listener.
        """
        # Create the graph.
        graph = {}
        server_address = ('localhost', 20000)
        print("\nStarting LISTENER, we receive messages on address 127.0.0.1, 20000")
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as listener:
            listener.bind(server_address)
            # utc_time_now = datetime.utcnow()

            while True:
                # print("\nblocking, waiting to receive message")
                incoming_data = listener.recv(4096)

                # print(f"received {len(incoming_data)} bytes")
                # print(incoming_data)

                # Parse the individual quotes from the message.
                messages = fxp_bytes_subscriber.unmarshall_message(incoming_data)

                # print(f"Unmarshall the messages {messages} from the Forex Provider.")
                # handle each quote in the quote list (list of dicts, ea dict is a quote)
                # 2019-10-14 23:58:36.216488 EUR USD 1.1005
                bf_graph = bellman_ford.BellmanFord(graph)
                for message in messages:
                    print(f"{message['timestamp']} {message['cross']} {message['price']}")
                    # """Add to the graph."""
                    curr2_to_curr1_rate = math.log(message['price'])
                    curr1_to_curr2_rate = -1 * curr2_to_curr1_rate

                    # create curr1 node if non-existing and add curr1 --> curr2 edge to graph
                    if curr1 not in graph:
                        graph[curr1] = {}
                    graph[curr1][curr2] = {"timestamp": message['timestamp'], "price": curr1_to_curr2_rate}

                    # create curr2 node if non-existing and add curr2 --> curr1 edge to graph
                    if curr2 not in graph:
                        graph[curr2] = {}
                    graph[curr2][curr1] = {"timestamp": curr_time, "price": curr2_to_curr1_rate}

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
