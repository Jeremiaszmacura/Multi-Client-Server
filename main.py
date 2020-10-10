"""The module contains the main program loop."""
import threading
import sys

from PyQt5 import QtWidgets

from gui import UiMainWindow


def start_gui():
    """Enabling GUI function."""
    app = QtWidgets.QApplication(sys.argv)
    ui = UiMainWindow()
    ui.set_up_ui()
    ui.MainWindow.show()
    sys.exit(app.exec_())


def main():
    """The main function of the program."""
    threading.Thread(target=start_gui).start()


if __name__ == '__main__':
    main()
