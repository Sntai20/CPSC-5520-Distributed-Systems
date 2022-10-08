"""
CPSC 5520, Seattle University
This is free and unencumbered software released into the public domain.
:Authors: Antonio Santana
:Version: 000-01

Expected output:
JOIN ('cs2.seattleu.edu', 23600)
HELLO to {'host': 'cs1.seattleu.edu', 'port': 10000}
('OK', "Happy to meet you, ('10.124.72.21', 38594)")
HELLO to {'host': 'cs2.seattleu.edu', 'port': 33313}
failed to connect: {} [Errno 111] Connection refused
HELLO to {'host': 'localhost', 'port': 23015}
('OK', "Happy to meet you, ('127.0.0.1', 44338)")
"""
import pickle
import socket
import sys

BUFFER_SIZE = 1024  # tcp receive buffer size


class Lab2():
    """
    Lab2 is used to join a group and meet members.
    """
    def __init__(self, gcd_host, gcd_port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((gcd_host, gcd_port))
        # JOIN ('cs2.seattleu.edu', 23600)
        print(f"JOIN ({gcd_host}, {gcd_port}")
        self.my_list = []

    def join_group(self):
        """
        Joins the incoming messages - expects only 'JOIN' messages
        """
        join_token = 'JOIN'
        self.my_list = self.message(self.socket, join_token, BUFFER_SIZE)
        self.socket.close()

    def meet_members(self):
        """
         The message to send to the other group members is just
         the text HELLO (also pickled, of course).
        """
        for item in self.my_list:
            host, port = item['host'], item['port']
            try:
                my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                my_socket.settimeout(1500)
                if host == "localhost":
                    host = "127.0.0.1"
                my_socket.connect((host, port))

                hello_token = 'HELLO'
                # HELLO to {'host': 'localhost', 'port': 23015}
                print(f"HELLO to {'host': '{host}', 'port': {port}}")
                my_message = self.message(my_socket, hello_token, BUFFER_SIZE)
                print(my_message)
                my_socket.close()

            except socket.gaierror as e_exception:
                print(f"Address-related error connecting to server: {e_exception}")
            except socket.error as e_exception:
                print(f"failed to connect: {e_exception}")
            except Exception as failure:
                print('general failure', failure)

    @staticmethod
    def message(sock, send_data, buffer_size):
        """
        Serialize the message using pickle.
        """
        response = pickle.dumps(send_data)
        sock.sendall(response)
        second_message = sock.recv(buffer_size)
        return_message = pickle.loads(second_message)
        return return_message


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python lab2.py GCDHOST GCDPORT")
        sys.exit(1)
    host, port = sys.argv[1:]
    lab2 = Lab2(host, int(port))
    lab2.join_group()
    lab2.meet_members()
