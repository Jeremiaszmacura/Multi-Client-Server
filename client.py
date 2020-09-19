"""Moduł zawiera klasę Client."""
import socket
from const import Consts


class Client:
    """Klasa Client zawiera metody potrzebne do obługi klienta."""

    def __init__(self):
        self.connected = False

    def create_socket(self):
        """Metoda tworzy socket."""
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print("[CLIENT] Socket creation error: " + str(msg))

    def connect_socket(self):
        """Metoda nawiązuje połączenie z serwerem."""
        try:
            self.client.connect(Consts.ADDR)
            self.connected = True
        except socket.error as msg:
            print("[CLIENT] Connecting socket error: " + str(msg))

    def send_message(self, msg):
        """Metoda wysyła wiadomości do serwera."""
        message = msg.encode(Consts.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(Consts.FORMAT)
        send_length += b' ' * (Consts.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(2048).decode(Consts.FORMAT))

    def receive_message(self):
        """Metoda odbiera wiadomości od serwera"""
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
    """Metoda zawiera testowe połączenie."""
    client = Client()
    client.create_socket()
    client.connect_socket()
    client.receive_message()


start_client()
