"""Moduł zawiera głowną petlę programu."""
import threading
import sys

from PyQt5 import QtWidgets

from gui import Ui_MainWindow

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