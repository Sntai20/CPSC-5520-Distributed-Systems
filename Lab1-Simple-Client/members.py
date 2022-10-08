"""
CPSC 5520, Seattle University
This is free and unencumbered software released into the public domain.
:Authors: Kevin Lundeen
:Version: f19-02
"""
import pickle
import socketserver
import sys
BUF_SZ = 1024  # tcp receive buffer size


class GroupMember1(socketserver.BaseRequestHandler):
    """
    A Group Member that acts as a server and responds to peers' messages
    For Lab1, we respond only to HELLO messages.
    """
    def handle(self):
        """
        Handles the incoming messages - expects only 'HELLO' messages
        """
        raw = self.request.recv(
            BUF_SZ)  # self.request is the TCP socket connected to the client
        try:
            message = pickle.loads(raw)
        except (pickle.PickleError, KeyError):
            response = bytes('Expected a pickled message, got ' +
                             str(raw)[:100] + '\n', 'utf-8')
        else:
            if message != 'HELLO':
                response = pickle.dumps('Unexpected message: ' + str(message))
            else:
                message = (f"OK, Happy to meet you, {self.client_address}")
                response = pickle.dumps(message)
        self.request.sendall(response)

class GroupMember2(socketserver.BaseRequestHandler):
    """
    A Group Member that acts as a server and responds to peers' messages
    For Lab1, we respond only to HELLO messages.
    """
    def handle(self):
        """
        Handles the incoming messages - expects only 'HELLO' messages
        """
        raw = self.request.recv(
            BUF_SZ)  # self.request is the TCP socket connected to the client
        try:
            message = pickle.loads(raw)
        except (pickle.PickleError, KeyError):
            response = bytes('Expected a pickled message, got ' +
                             str(raw)[:100] + '\n', 'utf-8')
        else:
            if message != 'HELLO':
                response = pickle.dumps('Unexpected message: ' + str(message))
            else:
                message = (f"OK, Happy to meet you, {self.client_address}")
                response = pickle.dumps(message)
        self.request.sendall(response)

class GroupMember3(socketserver.BaseRequestHandler):
    """
    A Group Member that acts as a server and responds to peers' messages
    For Lab1, we respond only to HELLO messages.
    """
    def handle(self):
        """
        Handles the incoming messages - expects only 'HELLO' messages
        """
        raw = self.request.recv(
            BUF_SZ)  # self.request is the TCP socket connected to the client
        try:
            message = pickle.loads(raw)
        except (pickle.PickleError, KeyError):
            response = bytes('Expected a pickled message, got ' +
                             str(raw)[:100] + '\n', 'utf-8')
        else:
            if message != 'HELLO':
                response = pickle.dumps('Unexpected message: ' + str(message))
            else:
                message = (f"OK, Happy to meet you, {self.client_address}")
                response = pickle.dumps(message)
        self.request.sendall(response)

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python members.py")
        exit(1)

    #member_list = ['21313', '33313', '23015']
    with socketserver.TCPServer(('', int("21313")), GroupMember1) as server:
        print("1")
        server.serve_forever()

    with socketserver.TCPServer(('', int("33313")), GroupMember2) as server:
        print("2")
        server.serve_forever()

    with socketserver.TCPServer(('', int("23015")), GroupMember3) as server:
        server.serve_forever() 
        print("3")
        #print(f"{member_port} Listener started")
