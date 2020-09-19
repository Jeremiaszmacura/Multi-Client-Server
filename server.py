"""Moduł zawiera klasę Server."""
import socket
import threading

from const import Consts


class Server:
    """Klasa serwera zawiera metody potrzebne do obługi serwera."""

    def __init__(self):
        self.running = False
        self.conn_list = {}
        self.recv_and_send_msg = []

    def create_socket(self):
        """Metoda tworzy socket."""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print("[SERVER] Socket creation error: " + str(msg))

    def bind_socket(self):
        """Metoda binduje socket."""
        try:
            self.server_socket.bind(Consts.ADDR)
        except socket.error as msg:
            print("[SERVER] Socket binding error: " + str(msg))

    def send_private_msg(self, addr, conn, text):
        """Metoda wysyła wiadomość do konkretnego użytkownika."""
        conn.send(text.encode(Consts.FORMAT))
        self.recv_and_send_msg.append(f"[SERVER] TO CLIENT {addr}: {text}")

    def handle_client(self, conn, addr):
        """Metoda utrzymuje połączenie z klientem."""
        connected = True
        try:
            while connected:
                msg_length = conn.recv(Consts.HEADER).decode(Consts.FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(Consts.FORMAT)
                    if msg == Consts.DISCONNECT_MESSAGE:
                        connected = False
                    self.recv_and_send_msg.append(f"[CLIENT] {addr} TO SERVER: {msg}")
                    print(f"[CLIENT] {addr}: {msg}")
                    conn.send("[SERVER] Message received.".encode(Consts.FORMAT))
        except:
            print("[SERVER] Client error: %s:%d" % (addr[0], addr[1]))

        self.conn_list.pop(addr)
        conn.close()

    def start(self):
        """Metoda nawiązuje połączenie z klienetem i tworzy nowe wątki."""
        self.server_socket.listen()
        print(f"[SERVER] Server is listening on {Consts.SERVER}")
        try:
            while self.running:
                conn, addr = self.server_socket.accept()
                self.conn_list[addr] = conn
                print("[SERVER] Connection accepted: %s:%d" % (addr[0], addr[1]))
                self.recv_and_send_msg.append("[SERVER] Connection accepted: %s:%d"
                                              % (addr[0], addr[1]))
                conn.send("Connection accepted.".encode(Consts.FORMAT))
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
        except socket.error:
            print("[SERVER] New connections are stopped.")
        except:
            print("[SERVER] Error start fun in server module.")

    def start_server(self):
        """Metoda tworzy nowy socket i nowy wątek."""
        self.create_socket()
        self.bind_socket()
        self.running = True
        print("[SERVER] Server is starting...")
        threading.Thread(target=self.start).start()

    def stop_server(self):
        """Metoda zamyka socket servera."""
        print("[SERVER] Server is stopped.")
        for connection in self.conn_list.values():
            connection.send(Consts.DISCONNECT_MESSAGE.encode(Consts.FORMAT))
        self.conn_list.clear()
        self.running = False
        self.server_socket.close()
