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
        self.gcd_host = gcd_host
        self.gcd_port = gcd_port
        self.gcd_address = (self.gcd_host, self.gcd_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.gcd_host, self.gcd_port))
        self.my_dictionary = {}
        self.my_list = []
        # self.listener, self.listener_address = self.start_a_server()

    def join_group(self):
        """
        Joins the incoming messages - expects only 'JOIN' messages
        ('JOIN', ((days_to_bd, su_id), (host, port)))
        """
        join_token = 'JOIN'
        days_to_bd = '10'
        su_id = '55555'
        message = f"'{join_token}', '(({days_to_bd}, {su_id}), ({self.gcd_host}, 0))'"
        print(f"This is the message we are sending {message}")
        self.my_dictionary = self.message(self.socket, message , BUFFER_SIZE)
        #print(f"Response is {self.my_dictionary}")
        self.socket.close()

    def meet_members(self):
        """
         The message to send to the other group members is just
         the text HELLO (also pickled, of course).
        """
        for dictionary_item in self.my_list:
            self.my_dictionary = dictionary_item
            #member_host = self.my_dictionary[0:1]
            #member_port = self.my_dictionary[1]
            print(self.my_dictionary[0:1])

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
        response = pickle.dumps(send_data)
        print(f"This is the pickled message we are sending {response}")
        sock.sendall(response)
        second_message = sock.recv(buffer_size)
        return_message = pickle.loads(second_message)
        print(f"This is the message we are receiving {return_message}")
        return return_message

    # @staticmethod
    # def start_a_server():
    #     try:
    #         process_id, listener = message_data
    #         listen_host, listen_port = listener
    #         days_to_birthday, student_id = process_id
    #     except (ValueError, TypeError):
    #         raise ValueError('Malformed message data, expected '
    #             + '((days_to_bd, su_id), (host, port))') from TypeError
    #     # make sure that listen_host is localhost or equivalent
    #     try:
    #         listen_ip = socket.gethostbyname(listen_host)
    #     except Exception as err:
    #         raise ValueError(str(err)) from err
    #     if not (isinstance(listen_port) is int and 0 < listen_port < 65_536):
    #         raise ValueError('Invalid port number')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python lab2.py GCDHOST GCDPORT")
        sys.exit(1)
    GCD_HOST = sys.argv[1]
    GCD_PORT = sys.argv[2]
    print(f"Using the following address: {GCD_HOST} {GCD_PORT}")

    lab2 = Lab2(GCD_HOST, int(GCD_PORT))
    lab2.join_group()
    #lab2.meet_members()
