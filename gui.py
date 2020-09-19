"""Moduł zawiera klasę GUI."""
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QTextEdit, QVBoxLayout, QMessageBox

from server import Server
from const import Consts


class Ui_MainWindow(object):
    """Klasa zawiera zmienne i metody tworzące GUI."""

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.widgets = QtWidgets.QWidget(self.MainWindow)
        self.layout = QtWidgets.QGridLayout(self.widgets)
        self.label_01 = QtWidgets.QLabel("{}".format(0, 0, 1, 1))
        self.label_02 = QtWidgets.QLabel("{}".format(1, 0, 1, 1))
        self.label_03 = QtWidgets.QLabel("{}".format(0, 1, 2, 1))
        self.label_04 = QtWidgets.QLabel("{}".format(2, 0, 1, 2))
        self.layout_connetion_list = QVBoxLayout(self.MainWindow)
        self.connection_list_widget = QTextEdit()
        self.timer_01 = QtCore.QTimer()
        self.timer_02 = QtCore.QTimer()
        self.font = QtGui.QFont('Times', 20, QFont.Bold)
        self.server = Server()

    def setupUi(self):
        """Metoda tworzy obiekty widgetów w odpowiednich kontenerach."""
        # Główne okno
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setFixedSize(800, 600)
        self.widgets.setObjectName("centralwidget")
        self.MainWindow.setCentralWidget(self.widgets)
        # Układ
        self.label_01.setStyleSheet("background-color: {}".format(Consts.LABEL_01_COLOR))
        self.layout.addWidget(self.label_01, 0, 0, 1, 1)
        self.label_02.setStyleSheet("background-color: {}".format(Consts.LABEL_02_COLOR))
        self.layout.addWidget(self.label_02, 1, 0, 1, 1)
        self.label_03.setStyleSheet("background-color: {}".format(Consts.LABEL_03_COLOR))
        self.layout.addWidget(self.label_03, 0, 1, 2, 1)
        self.label_04.setStyleSheet("background-color: {}".format(Consts.LABEL_04_COLOR))
        self.layout.addWidget(self.label_04, 2, 0, 1, 2)
        # Timer
        self.timer_01.setInterval(50)
        self.timer_02.setInterval(50)
        self.timer_01.timeout.connect(self.active_connection_list_gui)
        self.timer_02.timeout.connect(self.information_flow_gui_list)
        self.timer_01.start()
        self.timer_02.start()
        # Inicjalizacja zmiennych
        self.on_off_button = QtWidgets.QPushButton(self.widgets)
        self.on_off_img = QtWidgets.QLabel(self.widgets)
        self.label_server = QtWidgets.QLabel(self.widgets)
        self.on_off_info = QtWidgets.QLabel(self.widgets)
        self.label_client = QtWidgets.QLabel(self.widgets)
        self.send_button = QtWidgets.QPushButton(self.widgets)
        self.label_client_info = QtWidgets.QLabel(self.widgets)
        self.label_information_flow = QtWidgets.QLabel(self.widgets)
        # Wysyłanie wiadomości do klienta - label_02
        self.send_button.setGeometry(QtCore.QRect(125, 340, 150, 32))
        self.send_button.setCheckable(True)
        self.send_button.clicked.connect(self.take_send_inputs)
        self.label_client.setGeometry(QtCore.QRect(150, 230, 100, 32))
        self.font.setPointSize(26)
        self.label_client.setFont(self.font)
        self.label_client.setObjectName("label_server")
        self.label_client_info.setGeometry(QtCore.QRect(80, 285, 310, 32))
        self.label_client_info.setText("Send an information to client")
        self.label_client_info.setFont(QFont('Times', 16))
        # Przycisk on-off
        self.on_off_button.setGeometry(QtCore.QRect(80, 90, 81, 81))
        self.on_off_button.setObjectName("on_off_button")
        self.on_off_button.setIcon(QIcon("assets/icons8-shutdown-80"))
        self.on_off_button.setIconSize(QSize(80, 80))
        self.on_off_button.setStyleSheet("border: none;")
        self.on_off_button.setCheckable(True)
        self.on_off_button.clicked.connect(self.server_on_off)
        # Ikona pokazująca stan on-off
        self.on_off_img.setGeometry(QtCore.QRect(220, 110, 81, 51))
        self.on_off_img.setPixmap(QtGui.QPixmap("assets/icons8-toggle-off-80.png"))
        self.on_off_img.setObjectName("on_off_img")
        # Napis Server
        self.label_server.setGeometry(QtCore.QRect(150, 15, 100, 71))
        self.font.setPointSize(26)
        self.label_server.setFont(self.font)
        self.label_server.setObjectName("label_server")
        # Napis on-off
        self.on_off_info.setGeometry(QtCore.QRect(247, 160, 41, 16))
        self.font.setPointSize(12)
        self.on_off_info.setFont(self.font)
        self.on_off_info.setObjectName("on_off_info")
        # Pozostałe
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        """Funkcja ustawia napisy i tytuły widżetów."""
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Client-Server"))
        self.on_off_button.setText(_translate("MainWindow", ""))
        self.label_server.setText(_translate("MainWindow", "Server"))
        self.on_off_info.setText(_translate("MainWindow", "OFF"))
        self.label_client.setText(_translate("MainWindow", "Client"))
        self.send_button.setText(_translate("MainWindow", "Send"))
        self.label_01.setText(_translate("MainWindow", ""))
        self.label_02.setText(_translate("MainWindow", ""))
        self.label_03.setText(_translate("MainWindow", ""))
        self.label_04.setText(_translate("MainWindow", ""))

    def server_on_off(self):
        """Metoda odpowiada za włączanie i wyłączanie serwera."""
        if self.on_off_button.isChecked():
            self.on_off_img.setPixmap(QtGui.QPixmap("assets/icons8-toggle-on-80.png"))
            _translate = QtCore.QCoreApplication.translate
            self.on_off_info.setText(_translate("MainWindow", "ON"))
            self.server.start_server()
        else:
            self.on_off_img.setPixmap(QtGui.QPixmap("assets/icons8-toggle-off-80.png"))
            _translate = QtCore.QCoreApplication.translate
            self.on_off_info.setText(_translate("MainWindow", "OFF"))
            self.server.stop_server()

    def active_connection_list_gui(self):
        """Metoda wyświetla listę aktywnych połączeń."""
        self.label_03.setFont(QFont('Times', 18))
        if threading.activeCount() <= 2:
            self.label_03.setText("ACTIVE CONNETCTIONS \n\n\nServer is not running")
        else:
            temp_sting = "ACTIVE CONNETCTIONS ({})\n\n\n".format(threading.activeCount() - 3)
            for connection in self.server.CONN_LIST:
                temp_sting += str(connection) + "\n"
            self.label_03.setText(temp_sting)
        self.label_03.setAlignment(Qt.AlignCenter)

    def information_flow_gui_list(self):
        """Metoda wyświetla listę wysłanych i odebranych wiadomości."""
        self.label_04.setFont(QFont('Times', 14))
        temp_string = "Information flow\n\n"
        for msg in self.server.recv_and_send_msg:
            temp_string += str(msg) + "\n"
        self.label_04.setText(temp_string)
        self.label_04.setAlignment(Qt.AlignCenter)

    def take_send_inputs(self):
        """Funkcja zbiera i obsługuje dane zebrane po przysiskien Send."""
        if not self.on_off_button.isChecked():
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("Server is not running")
            warning.setWindowTitle("Server is OFF")
            warning.setStandardButtons(QMessageBox.Ok)
            return_value = warning.exec()
            if return_value == QMessageBox.Ok:
                pass
            return
        ip = QtWidgets.QInputDialog.getText(self.widgets, 'Input Dialog', 'Enter client ip:')
        port = QtWidgets.QInputDialog.getInt(self.widgets, 'Input Dialog', 'Enter client port:')
        message = QtWidgets.QInputDialog.getText(self.widgets, 'Input Dialog', 'Enter message:')
        message = message[0]
        addr = (ip[0], port[0])
        try:
            conn = self.server.CONN_LIST[addr]
            self.server.send_private_msg(addr, conn, message)
        except:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("Wrong client ip or port")
            warning.setWindowTitle("Incorrect Data")
            warning.setStandardButtons(QMessageBox.Ok)
            return_value = warning.exec()
            if return_value == QMessageBox.Ok:
                pass
            return
