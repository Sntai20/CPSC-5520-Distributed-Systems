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
from datetime import datetime
from enum import Enum
import pickle
import socket
import sys

BUFFER_SIZE = 1024  # tcp receive buffer size

class MessageName(Enum):
    """Enum of all the message names."""
    JOIN = 1
    ELECTION = 2
    COORDINATOR = 3
    PROBE = 4


class Lab2():
    """
    Lab2 is used to join a group and meet members.
    """
    def __init__(self, gcd_host, gcd_port, next_birthday, student_id):
        """
        param: gcd_host localhost or 127.0.0.1
        param: gcd_port 23633
        param: next_birthday YYYY-MM-DD
        param: student_id 123456
        """
        self.gcd_address = (gcd_host, gcd_port)
        days_to_birthday = (datetime.fromisoformat(next_birthday) - datetime.now()).days
        self.process_id = (days_to_birthday, int(student_id))
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(self.gcd_address)
        self.members_list = []
        self.listener, self.listener_address = self.start_a_server()

    @staticmethod
    def start_a_server():
        """
        Start up a listening server, use 0 to bind to any open port,
        set the backlog to 100, and do not block the socket.

        return: A listener.
        """
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind(('localhost', 0))
        listener.listen(100)
        listener.setblocking(False)
        return listener, listener.getsockname()

    def join_group(self):
        """
        ('JOIN', ((days_to_bd, su_id), (host, port)))

        All messages are pickled and are a pair (message_name, message_data),
        where message_name is the text of the message name (that is, one of
        'JOIN', 'ELECTION', 'COORDINATOR', or 'PROBE') and the message_data
        is specified in the protocol below or, if there is no message data,
        use None. Message responses, when they exist, can either be just
        pickled text or data as specified in the protocol below.
        """
        message_data = (self.process_id, self.listener_address)
        message = MessageName(1).name, message_data
        print(f"This is the message we are sending {message}")
        self.members_list = self.message(self.socket, message , BUFFER_SIZE)
        self.socket.close()

    def meet_members(self):
        """
         The message to send to the other group members is just
         the text HELLO (also pickled, of course).
        """
        for member_dictionary_item in self.members_list:
            # member_dictionary_item
            #member_host = self.my_dictionary[0:1]
            #member_port = self.my_dictionary[1]
            print(member_dictionary_item[0:1])

            # #member_host, member_port = dictionary_item['host'], dictionary_item['port']
            # try:
            #     my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #     my_socket.settimeout(1500)
            #     my_socket.connect((member_host, member_port))

            #     hello_token = 'HELLO'
            #     # HELLO to {'host': 'localhost', 'port': 23015}
            #     print(f"HELLO to {'host': '{member_host}', 'port': {member_port}}")
            #     my_message = self.message(my_socket, hello_token, BUFFER_SIZE)
            #     print(my_message)
            #     my_socket.close()

            # except ConnectionRefusedError as e_exception:
            #     print(f"{member_host}: {e_exception}")
            # except socket.gaierror as e_exception:
            #     print(f"Address-related error connecting to server: {e_exception}")
            # except socket.error as e_exception:
            #     print(f"failed to connect: {e_exception}")

    @staticmethod
    def message(sock, send_data, buffer_size):
        """
        Serialize the message using pickle.
        """
        sock.sendall(pickle.dumps(send_data))
        received_response_data = sock.recv(buffer_size)
        return_message = pickle.loads(received_response_data)
        print(f"This is the message we are receiving {return_message}")
        return return_message

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python lab2.py GCDHOST GCDPORT YYYY-MM-DD SUID")
        print("Birthday format is YYYY-MM-DD")
        sys.exit(1)
    
    GCD_HOST = sys.argv[1]
    GCD_PORT = sys.argv[2]
    NEXT_BIRTHDAY = sys.argv[3]
    STUDENT_ID = sys.argv[4]
    print(f"Using the following address: {GCD_HOST} {GCD_PORT} {NEXT_BIRTHDAY} {STUDENT_ID}")

    lab2 = Lab2(GCD_HOST, int(GCD_PORT), NEXT_BIRTHDAY, STUDENT_ID)
    lab2.join_group()
    #lab2.meet_members()
