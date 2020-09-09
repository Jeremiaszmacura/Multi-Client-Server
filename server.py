"""Moduł zawiera klasę Server."""
import socket
import threading
from const import Consts

class Server:
    """Klasa serwera zawiera metody potrzebne do obługi serwera."""
    def __init__(self):
        self.running = False
        self.PORT = 2121
        self.SERVER = '192.168.1.103'
        self.ADDR = (self.SERVER, self.PORT)
        self.CONN_LIST = {}

    def create_socket(self):
        """Metoda tworzy socket."""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print("Socket creation error: " + str(msg))

    def bind_socket(self):
        """Metoda binduje socket."""
        try:
            self.server_socket.bind(self.ADDR)
        except:
            print("Binding socket error")

    def active_conn(self):
        print(f"[ACTIVE CONNETCTIONS] {threading.activeCount() - 1}")
        for x in self.CONN_LIST:
            print(x)

    def send_private_msg(self, conn):
        conn.send("private message.".encode(Consts.FORMAT))

    def handle_client(self, conn, addr):
        """Metoda utrzymuje połączenie z klientem."""
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True
        try:
            while connected:
                msg_length = conn.recv(Consts.HEADER).decode(Consts.FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(Consts.FORMAT)
                    if msg == Consts.DISCONNECT_MESSAGE:
                        connected = False

                    print(f"[{addr}] {msg}")
                    conn.send("Msg received".encode(Consts.FORMAT))
        except:
            print("Client error: %s:%d" % (addr[0], addr[1]))

        self.CONN_LIST.pop(addr)
        conn.close()

    def start(self):
        """Metoda nawiązuje połączenie z klienetem i tworzy nowe wątki."""
        self.server_socket.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        try:
            while self.running:
                conn, addr = self.server_socket.accept()
                self.CONN_LIST[addr] = conn
                print("[CONNECTION ACCEPTED]: %s:%d" % (addr[0], addr[1]))
                conn.send("Msg received".encode(Consts.FORMAT))
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                self.active_conn()
        except:
            print("Error start fun in server module")

    def start_server(self):
        """Metoda tworzy nowy socket i nowy wątek."""
        self.create_socket()
        self.bind_socket()
        print("[STARTING] server is starting...")
        threading.Thread(target=self.start).start()

    def stop_server(self):
        """Metoda zamyka socket servera."""
        print("[STOP] server is stopped.")
        self.server_socket.close()
