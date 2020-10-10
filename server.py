"""The module contains the Server class."""
import socket
import threading

from const import Consts


class Server:
    """The server class contains the methods needed to operate the server."""

    def __init__(self):
        self.running = False
        self.conn_list = {}
        self.recv_and_send_msg = []

    def create_socket(self):
        """The method creates a socket."""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print("[SERVER] Socket creation error: " + str(msg))

    def bind_socket(self):
        """The method binds socket."""
        try:
            self.server_socket.bind(Consts.ADDR)
        except socket.error as msg:
            print("[SERVER] Socket binding error: " + str(msg))

    def send_private_msg(self, addr, conn, text):
        """The method sends a message to a specific user."""
        conn.send(text.encode(Consts.FORMAT))
        self.recv_and_send_msg.append(f"[SERVER] TO CLIENT {addr}: {text}")

    def handle_client(self, conn, addr):
        """The method maintains the connection with the client."""
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
        """The method provide connection to the client and creates new threads."""
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
        """The method creates a new socket and a new thread."""
        self.create_socket()
        self.bind_socket()
        self.running = True
        print("[SERVER] Server is starting...")
        threading.Thread(target=self.start).start()

    def stop_server(self):
        """The method closes the server socket."""
        print("[SERVER] Server is stopped.")
        for connection in self.conn_list.values():
            connection.send(Consts.DISCONNECT_MESSAGE.encode(Consts.FORMAT))
        self.conn_list.clear()
        self.running = False
        self.server_socket.close()
