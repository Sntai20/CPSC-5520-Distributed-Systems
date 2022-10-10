"""
CPSC 5520, Seattle University
This is free and unencumbered software released into the public domain.
:Authors: Antonio Santana
:Version: 000-01

Expected output:
"""
from datetime import datetime
from enum import Enum
import pickle
import selectors
import socket
import sys

BUFFER_SIZE = 1024  # tcp receive buffer size
CHECK_INTERVAL = 1

class MessageName(Enum):
    """Enum of all the message names."""
    JOIN = 1
    ELECTION = 2
    COORDINATOR = 3
    PROBE = 4

class State(Enum):
    """
    Enumeration of states a peer can be in for the Lab2 class.
    """
    QUIESCENT = 'QUIESCENT'  # Erase any memory of this peer

    # Outgoing message is pending
    SEND_ELECTION = 'ELECTION'
    SEND_VICTORY = 'COORDINATOR'
    SEND_OK = 'OK'

    # Incoming message is pending
    WAITING_FOR_OK = 'WAIT_OK'  # When I've sent them an ELECTION message
    WAITING_FOR_VICTOR = 'WHO IS THE WINNER?'  # This one only applies to myself
    WAITING_FOR_ANY_MESSAGE = 'WAITING'  # When I've done an accept on their connect to my server

    def is_incoming(self):
        """Categorization helper."""
        return self not in (State.SEND_ELECTION, State.SEND_VICTORY, State.SEND_OK)

class Lab2():
    """
    Lab2 is used to join a group and meet members.
    """
    def __init__(self, next_birthday, student_id):
        """
        param: gcd_host localhost or 127.0.0.1
        param: gcd_port 23633
        param: next_birthday YYYY-MM-DD
        param: student_id 123456
        gcd_address consists of gcd_host and gcd_port

        """
        days_to_birthday = (datetime.fromisoformat(next_birthday) - datetime.now()).days
        self.process_id = (days_to_birthday, int(student_id))
        self.members_list = []
        self.states = {}
        self.bully = None
        self.selector = selectors.DefaultSelector()
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
        # Setup the socket here.
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect(GCD_ADDRESS)
        self.members_list = self.message(mysocket, message , BUFFER_SIZE)
        mysocket.close()

    def run(self):
        """
        Runs event loop
        """

        # register MY listening socket
        self.selector.register(self.listener, selectors.EVENT_READ)

        # selector loop
        while True:
            events = self.selector.select(CHECK_INTERVAL)

            print(events)

            for key, mask in events:
                if key.fileobj == self.listener:  # accept peer
                    print(f"key, mask {key}, {mask}")
                    self.accept_peer()
            #     elif mask and selectors.EVENT_READ:  # recv msg
            #         self.receive_message(key.fileobj)
            #     else:  # mask and selectors.EVENT_WRITE
            #         self.send_message(key.fileobj)  # send msg
            # self.check_timeouts()

    def accept_peer(self):
        """
        Accept new TCP/IP connections from a peer (TCP handshake)
        """
        print('in accept_peer')
        try:
            peer, address = self.listener.accept()
            print(f"{peer}: accepted {address})")
            # self.set_state(State.WAITING_FOR_ANY_MESSAGE, peer)
        # except socket_error as serr:
        #     print(f"Accept failed {serr}")
        except ConnectionRefusedError as e_exception:
            print(f"peer : {e_exception}")
        except socket.gaierror as e_exception:
            print(f"Address-related error connecting to server: {e_exception}")
        except socket.error as e_exception:
            print(f"failed to connect: {e_exception}")

    def start_election(self):
        """
         The message to send to the other group members is just
         the text HELLO (also pickled, of course).
        """
        print("Start an election with the members in the member list.")
        for member_process_id_dictionary in self.members_list:
            # Am I in this list?
            if member_process_id_dictionary == self.process_id:
                print(f"My Process ID {self.process_id}")
                continue

            if member_process_id_dictionary[0] > self.process_id[0]:
                print(f"Member's Process ID {member_process_id_dictionary} " +
                    f"is higher than mine {self.process_id}. Send them a message.")
            else:
                print(f"Member's Process ID {member_process_id_dictionary} " +
                    f"is lower than mine {self.process_id}. No need to send them a message.")

            # print(f"Member Process ID: {member_process_id_dictionary}")
            # member_days_to_birthday, member_student_id = member_process_id_dictionary
            # print(member_days_to_birthday)
            # print(member_student_id)
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
        # print(f"This is the message we are receiving {return_message}")
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
    GCD_ADDRESS = GCD_HOST, int(GCD_PORT)
    # print(f"Using the following address: {GCD_HOST} {GCD_PORT} {NEXT_BIRTHDAY} {STUDENT_ID}")

    lab2 = Lab2(NEXT_BIRTHDAY, STUDENT_ID)
    lab2.join_group()
    lab2.start_election()
