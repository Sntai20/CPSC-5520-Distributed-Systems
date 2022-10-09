"""
CPSC 5520, Seattle University
This is free and unencumbered software released into the public domain.
:Authors: Kevin Lundeen
:Version: f19-02
"""
import pickle
import socket
import socketserver
import sys

BUF_SZ = 1024  # tcp receive buffer size

class GroupCoordinatorDaemon(socketserver.BaseRequestHandler):
    """
    A Group Coordinator Daemon (GCD) which will respond with a
    list of potential group members to a text message JOIN
    with list of group members to contact.

    We respond with a dictionary of group members.
    """
    # global group data structures
    # listener address indexed by process id (as returned from JOIN message)
    listeners_by_pid = {}
    # process ids indexed by listener address (only one pid for each unique (host, port))
    pids_by_listener = {}
    # process ids indexed by student id (each student only allowed one at a time)
    pids_by_student = {}
    # we want to restrict all listeners to be on the same host as the GCD
    localhost_ip = socket.gethostbyname('localhost')

    def handle(self):
        """
        Handles the incoming messages - expects only 'JOIN' messages
        """
        print(self.request.getsockname())
        raw = self.request.recv(BUF_SZ)  # self.request is the TCP socket connected to the client
        try:
            message = pickle.loads(raw)
            # Remove this line after testing.
            print(f"From handle function {message}")
        except pickle.PickleError:
            # https://pythontic.com/modules/pickle/exceptions
            response = bytes('Expected a pickled message, got ' + str(raw)[:100] + '\n', 'utf-8')
        except Exception:
            response = bytes('Expected a pickled message, got ' + str(raw)[:100] + '\n', 'utf-8')
        else:
            try:
                response_data = self.handle_join(message)
                # Remove this line after testing.
                print(f"From handle function try handle_join response data {response_data}")
            except ValueError as err:
                response_data = str(err)
            response = pickle.dumps(response_data)
        self.request.sendall(response)
        # Remove this line after testing.
        print(f"From handle function response data {response_data}")
        self.request.shutdown(socket.SHUT_RDWR)
        self.request.close()

    @staticmethod
    def handle_join(message):
        """
        Process this JOIN message by adding new member into the group data
        structures.

        Also do some validation:
        - of the right form
        - listener is on localhost (or equivalent)
        :param message: ('JOIN', ((days_to_bd, su_id), (host, port)))
        :return: GroupCoordinatorDaemon.listeners_by_pid
        :raises ValueError: if the message cannot be validated
        """
        try:
            # Remove this line after testing.
            print(f"handle_join message {message}")
            # pull apart message
            message_name, message_data = message
            # Remove this line after testing.
            print(f"handle_join message_name {message_name} message_data {message_data} = message {message}")
        except (ValueError, TypeError):
            raise ValueError('Malformed message') from TypeError
        if message_name != 'JOIN':
            raise ValueError(f'Unexpected message: {message_name}')

        # pull apart message_data
        try:
            # Delete after test
            print(f"Pull apart message_data {message_data}")
            process_id, listener = message_data
            print(process_id)
            print(listener)
            listen_host, listen_port = listener
            days_to_birthday, student_id = process_id
        except (ValueError, TypeError):
            raise ValueError('Malformed message data, expected '
                + '((days_to_bd, su_id), (host, port))') from TypeError
        if not (isinstance(days_to_birthday, int) and isinstance(student_id, int) and
                0 < days_to_birthday < 366 and 1_000_000 <= student_id < 10_000_000):
            raise ValueError('Malformed process id, expected (days_to_next_birthday, student_id)')
        # make sure that listen_host is localhost or equivalent
        try:
            listen_ip = socket.gethostbyname(listen_host)
        except Exception as err:
            raise ValueError(str(err)) from err
        if not (isinstance(listen_port, int) and 0 < listen_port < 65_536):
            raise ValueError('Invalid port number')
        if listen_ip != GroupCoordinatorDaemon.localhost_ip:
            raise ValueError('Only local group members currently allowed')
        listener = (listen_ip, listen_port)
        # aliases for global dictionaries
        students = GroupCoordinatorDaemon.pids_by_student
        group = GroupCoordinatorDaemon.listeners_by_pid
        listeners = GroupCoordinatorDaemon.pids_by_listener
        # remove any old memberships for the same student
        if student_id in students and students[student_id] != process_id:
            old_pid = students[student_id]
            del group[old_pid]
        students[student_id] = process_id
        # add this entry into group membership
        group[process_id] = listener
        # also remove any old memberships which claimed this same listener (host,port) pair
        if listener in listeners and listeners[listener] != process_id:
            old_pid = listeners[listener]
            if old_pid in group:
                del group[old_pid]
        listeners[listener] = process_id
        return group

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python gcd2.py GCDPORT")
        sys.exit(1)
    PORT = int(sys.argv[1])
    with socketserver.TCPServer(('', PORT), GroupCoordinatorDaemon) as server:
        server.serve_forever()
