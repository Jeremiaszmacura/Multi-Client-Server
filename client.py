"""Moduł zawiera klasę Client."""
import socket
from const import Consts

class Client():
    """Klasa Client zawiera metody potrzebne do obługi klienta."""
    def __init__(self):
        self.PORT = 2121
        self.SERVER = '192.168.1.103'
        self.ADDR = (self.SERVER, self.PORT)

    def create_socket(self):
        """Metoda tworzy socket."""
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print("Socket creation error: " + str(msg))

    def connect_socket(self):
        """Metoda nawiązuje połączenie z serwerem."""
        try:
            self.client.connect(self.ADDR)
        except:
            print("Connecting socket error")

    def send(self, msg):
        """Metoda wysyła wiadomości do serwera."""
        message = msg.encode(Consts.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(Consts.FORMAT)
        send_length += b' ' * (Consts.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(2048).decode(Consts.FORMAT))


