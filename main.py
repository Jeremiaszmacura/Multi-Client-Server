import threading
import sys

from PyQt5 import QtWidgets

from client import Client
from const import Consts
from gui import Ui_MainWindow

def start_client():
    client = Client()
    client.create_socket()
    client.connect_socket()
    client.send("Hello World!")
    input()
    client.send("Nygga")
    input()
    client.send(Consts.DISCONNECT_MESSAGE)

def start_gui():
    """Funkcja main programu."""
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.MainWindow.show()
    sys.exit(app.exec_())

def main():
    threading.Thread(target=start_gui).start()

if __name__ == '__main__':
    main()