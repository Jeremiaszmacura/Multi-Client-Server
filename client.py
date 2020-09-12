"""Moduł zawiera klasę Client."""
import socket
from const import Consts


class Client():
    """Klasa Client zawiera metody potrzebne do obługi klienta."""

    def __init__(self):
        self.connected = False
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
            self.connected = True
        except:
            print("Connecting socket error")

    # def handle_client(self, conn, addr):
    #     """Metoda utrzymuje połączenie z klientem."""
    #     print(f"[NEW CONNECTION] {addr} connected.")
    #     connected = True
    #     try:
    #         while connected:
    #             msg_length = conn.recv(Consts.HEADER).decode(Consts.FORMAT)
    #             if msg_length:
    #                 msg_length = int(msg_length)
    #                 msg = conn.recv(msg_length).decode(Consts.FORMAT)
    #                 if msg == Consts.DISCONNECT_MESSAGE:
    #                     connected = False
    #                 print(f"[{addr}] {msg}")
    #                 conn.send("[Server] Msg received".encode(Consts.FORMAT))
    #     except:
    #         print("Client error: %s:%d" % (addr[0], addr[1]))
    #
    #     self.CONN_LIST.pop(addr)
    #     conn.close()

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
            while self.connected:
                command = self.client.recv(1024)
                if command == Consts.DISCONNECT_MESSAGE:
                    self.connected = False
                print(command)
                self.send_message("[Client] Msg received!")


def start_client():
    """Metoda zawiera testowe połączenie."""
    client = Client()
    client.create_socket()
    client.connect_socket()
    client.receive_message()


start_client()
