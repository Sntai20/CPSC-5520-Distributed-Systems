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

class MessagingServiceSubscriber():
    def create_subscriber_client(self):
        server_address = ('localhost', 10000)
        print('starting up on {} port {}'.format(*server_address))

        # Create a UDP socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind(server_address)  # subscriber binds the socket to the publishers address
            while True:
                print('\nblocking, waiting to receive message')
                data = sock.recv(4096)

                print('received {} bytes'.format(len(data)))
                print(data)

if __name__ == '__main__':
    subscriber = MessagingServiceSubscriber()
    subscriber.create_subscriber_client()
