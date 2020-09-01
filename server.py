"""Moduł zawiera klasę Server."""
import socket
import threading
from const import Consts

class Server:
    """Klasa serwera zawiera metody potrzebne do obługi serwera."""
    def __init__(self):
        self.PORT = 2121
        self.SERVER = '192.168.1.103'
        self.ADDR = (self.SERVER, self.PORT)
        self.CONN_LIST = {}

    def create_socket(self):
        """Metoda tworzy socket."""
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print("Socket creation error: " + str(msg))

    def bind_socket(self):
        """Metoda binduje socket."""
        try:
            self.server.bind(self.ADDR)
        except:
            print("Binding socket error")

    def active_conn(self):
        print("Wypisuje liste aktywnych polaczen:")
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

        self.CONN_LIST.pop(addr)  # usuwamy socket z listy aktywnych połączeń
        conn.close()  # zamykamy połączenie

    def start(self):  # handle new connection
        """Metoda nawiązuje połączenie z klienetem i tworzy nowe wątki."""
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        try:
            while True:
                conn, addr = self.server.accept()  # conn = socket that alowes us to connect back,
                # addr = informaton about connection (port, ip adress)
                self.CONN_LIST[addr] = conn
                print("[CONNECTION ACCEPTED]: %s:%d" % (addr[0], addr[1]))
                conn.send("Msg received".encode(Consts.FORMAT))
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                self.active_conn()
        except:
            print("Error start fum")

def main():
    """Funkcja main programu."""
    print("[STARTING] server is starting...")
    server = Server()
    server.create_socket()
    server.bind_socket()
    server.start()

if __name__ == '__main__':
    main()