"""Moduł zawiera głowną petlę programu."""
import threading
import sys

from PyQt5 import QtWidgets

from gui import UiMainWindow


def start_gui():
    """Funkcja włączająca GUI."""
    app = QtWidgets.QApplication(sys.argv)
    ui = UiMainWindow()
    ui.set_up_ui()
    ui.MainWindow.show()
    sys.exit(app.exec_())


def main():
    """Funkcja main programu"""
    threading.Thread(target=start_gui).start()


if __name__ == '__main__':
    main()
