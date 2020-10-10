"""The module contains the Client class."""
import socket
from const import Consts


class Client:
    """The Client class contains the methods needed to service the client."""

    def __init__(self):
        self.connected = False

    def create_socket(self):
        """The method creates a socket."""
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print("[CLIENT] Socket creation error: " + str(msg))

    def connect_socket(self):
        """The method connects to the server."""
        try:
            self.client.connect(Consts.ADDR)
            self.connected = True
        except socket.error as msg:
            print("[CLIENT] Connecting socket error: " + str(msg))

    def send_message(self, msg):
        """The method sends messages to the server."""
        message = msg.encode(Consts.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(Consts.FORMAT)
        send_length += b' ' * (Consts.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(2048).decode(Consts.FORMAT))

    def receive_message(self):
        """The method receives messages from the server."""
        while self.connected:
            try:
                command = self.client.recv(1024).decode(Consts.FORMAT)
                if command == Consts.DISCONNECT_MESSAGE:
                    self.connected = False
                print("[SERVER] " + str(command))
                self.send_message("Msg received.")
            except:
                print("[CLIENT] receive_message function error.")
        self.client.close()


def start_client():
    """The method includes a connection test."""
    client = Client()
    client.create_socket()
    client.connect_socket()
    client.receive_message()


start_client()
