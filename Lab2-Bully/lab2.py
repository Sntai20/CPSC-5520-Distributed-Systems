"""
CPSC 5520, Seattle University
This is free and unencumbered software released into the public domain.
:Authors: Antonio Santana
:Version: 000-01
"""

from datetime import datetime
from enum import Enum
import pickle
import selectors
import socket
import sys

# tcp receive buffer size
BUFFER_SIZE = 1024
ASSUME_FAILURE_TIMEOUT = 5
CHECK_INTERVAL = 1
PEER_DIGITS = 1

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
                elif mask and selectors.EVENT_READ:  # recv msg
                    self.receive_message(key.fileobj)
                else:  # mask and selectors.EVENT_WRITE
                    self.send_message(key.fileobj)  # send msg
            self.check_timeouts()

    def accept_peer(self):
        """
        Accept new TCP/IP connections from a peer (TCP handshake)
        """
        print('in accept_peer')
        try:
            peer, address = self.listener.accept()
            print(f"{peer}: accepted {address})")
            self.set_state(State.WAITING_FOR_ANY_MESSAGE, peer)
        except ConnectionRefusedError as e_exception:
            print(f"peer : {e_exception}")
        except socket.gaierror as e_exception:
            print(f"Address-related error connecting to server: {e_exception}")
        except socket.error as e_exception:
            print(f"failed to connect: {e_exception}")

    def receive_message(self, peer):
        """
        Used to receive messages from other members.
        """

    @staticmethod
    def receive(peer, buffer_siz=BUFFER_SIZE):
        """
        Used to receive messages from other members.
        """

    def check_timeouts(self):
        """
        Checks my state to see if we are timedout.
        """

    def get_connection(self, member_pid):
        """
        Used to lookup the connections to other members.
        """
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # print(f" self.members_list[member_pid] {self.members_list[member_pid]}")
        new_socket.connect(self.members_list[member_pid])
        new_socket.setblocking(False)
        return new_socket

    def is_election_in_progress(self):
        """
        Checks my state to see if we are awaiting a victor.
        """
        if self.states[self.process_id] == State.WAITING_FOR_VICTOR:
            return True
        return False

    def is_expired(self, peer=None, threshold=ASSUME_FAILURE_TIMEOUT):
        """
        Checks my state to see if we are waiting
        for the responses too long, then uses timeout.
        """

    def set_leader(self, new_leader):
        """
        Empty bully dict and store newest bully by {pid : new_leader}
        """
        self.bully.clear()
        self.bully[new_leader.pid] = new_leader

    def get_state(self, peer=None, switch_mode=False):
        """
        Look up member's current state in state table.
        :param peer: socket connected to peer process (None means self)
        :param switch_mode: if True, then state and timestamp are both returned
        :return: either the state or (state, timestamp) depending on the detail (not
        found gives(QUIESCENT, None))
        """

        if not switch_mode:
            peer = self
        status = self.states[peer] if peer in self.states else (State.QUIESCENT, None)
        return status if switch_mode else status[0]

    def send_message(self, peer):
        """
        Send the queued msg to the given peer (based on its current state

        :param peer:
        :return:
        """

        state = self.get_state(peer)
        print(f'{self.pr_sock(peer)}: sending {state.value} {self.pr_now()}')
        try:
            # should be ready, but may be a failed connect instead
            self.send(peer, state.value, self.members_list)

        except ConnectionError as err:
            print(f'error sending exiting send_msg {err}')
        # except Exception as err:
        #     print(f'error sending exiting send_msg {err}')

        # check to see if we want to wait for response immediately
        if state == State.SEND_ELECTION:
            self.set_state(State.WAITING_FOR_OK, peer, switch_mode=True)
        else:
            self.set_quiescent(peer)

    def send(self, peer, message_name, message_data=None, wait_for_reply=False,
             buffer_size=BUFFER_SIZE):
        """
        Send the queued msg to the given peer (based on its current state

        :param peer:
        :return:
        """

        if self.is_election_in_progress():
            message_name = self.get_state(self)
            self.set_state(State.WAITING_FOR_OK)

        peer.sendall(pickle.dumps((message_name, message_data)))

        # register
        self.selector.register(peer, selectors.EVENT_READ)

    # def start_election(self):
    #     """
    #      The message to send to the other group members is just
    #      the text HELLO (also pickled, of course).
    #     """
    #     print("Start an election with the members in the member list.")
    #     for member_process_id_dictionary in self.members_list:
    #         # Am I in this list?
    #         if member_process_id_dictionary == self.process_id:
    #             print(f"My Process ID {self.process_id}")
    #             continue

            # if member_process_id_dictionary[0] > self.process_id[0]:
            #     print(f"Member's Process ID {member_process_id_dictionary} " +
            #         f"is higher than mine {self.process_id}. Send them a message.")
    #         else:
    #             print(f"Member's Process ID {member_process_id_dictionary} " +
    #                 f"is lower than mine {self.process_id}. No need to send them a message.")

    def start_election(self):
        """ Send ELECTION message to all peers that are bigger than me"""
        print('in start_election')
        # set state
        self.set_state(State.SEND_ELECTION)

        is_leader = True

        # check if I'm the leader
        for member_pid in self.members_list:
            print(member_pid)

            # skip myself
            if member_pid == self.process_id:
                continue

        # logic to only send election msgs to peers with pids greater than mine
        for member_pid in self.members_list:
            if member_pid == self.process_id:  # skip myself
                continue

            if member_pid[0] > self.process_id[0]:
                print(f"Member's Process ID {member_pid} " +
                    f"is higher than mine {self.process_id}. Send them a message.")

            # for peers greater than me
            if member_pid[0] > self.process_id[0] or \
                    (member_pid[0] == self.process_id[0] and member_pid[1] > self.process_id[1]):
                print(f" self.get_connection[member_pid] {self.members_list[member_pid[0]]}")
                # new_socket = self.get_connection(member_pid)
                # self.send_message(new_socket)  # send 'ELECTION'

    def set_state(self, state, peer=None, switch_mode=False):
        """
        Set a member's state in the state table.
        :param peer: socket connected to peer process (None means self)
        :param switch_mode: if True, then state and timestamp are both returned
        """

        if not switch_mode:
            peer = self
        self.states[peer] = state

    def set_quiescent(self, peer=None):
        """ call when you've sent an election out and didn't hear back in time from
        this peer, then update their state """
        if not peer:
            peer = self
        self.set_state(State.QUIESCENT, peer)

    def declare_victory(self, reason):
        """Send COORDINATOR message to all nodes."""

    def update_members(self, their_idea_of_membership):
        """Update my state to reflect the current members."""

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

    # def set_state(self, state, peer=None, switch_mode=False):
    #     """
    #     Set a member's state in the state table.
    #     :param peer: socket connected to peer process (None means self)
    #     :param switch_mode: if True, then state and timestamp are both returned
    #     """

    #     if not switch_mode:
    #         peer = self
    #     self.states[peer] = state

    @staticmethod
    def pr_now():
        """ Printing helper for current timestamp """
        return datetime.now().strftime('%H:%M:%S.%f')

    def pr_sock(self, sock):
        """Printing helper for given socket"""
        if sock is None or sock == self or sock == self.listener:
            return 'self'
        return self.cpr_sock(sock)

    @staticmethod
    def cpr_sock(sock):
        """Static version of helper for printing given socket"""
        l_port = sock.getsockname()[1] % PEER_DIGITS

        try:
            r_port = sock.getpeername()[1] % PEER_DIGITS
        except OSError:
            r_port = '???'
        return f'{l_port}->{r_port} ({id(sock)})'

    def pr_leader(self):
        """Print the current leader's name."""
        if self.bully == self.process_id:
            return 'self'
        # self.bully is None:
        return 'unknown'

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

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python lab2.py GCDHOST GCDPORT YYYY-MM-DD SUID")
        print("python3 lab2.py localhost 23633 2022-11-01 1234567")
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
