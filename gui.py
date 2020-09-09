"""Moduł zawiera klasę GUI."""
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon

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
        self.timer = QtCore.QTimer()
        self.font = QtGui.QFont()
        self.server = Server()

    def setupUi(self):
        """Metoda tworzy obiekty widgetów w odpowiednich kontenerach."""
        # Główne okno
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(800, 600)
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
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.active_connection_list_gui)
        self.timer.start()
        # Inicjalizacja zmiennych
        self.on_off_button = QtWidgets.QPushButton(self.widgets)
        self.on_off_img = QtWidgets.QLabel(self.widgets)
        self.label_server = QtWidgets.QLabel(self.widgets)
        self.on_off_info = QtWidgets.QLabel(self.widgets)
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
        self.label_server.setGeometry(QtCore.QRect(160, 10, 100, 71))
        self.font.setPointSize(20)
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
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.on_off_button.setText(_translate("MainWindow", ""))
        self.label_server.setText(_translate("MainWindow", "Server"))
        self.on_off_info.setText(_translate("MainWindow", "OFF"))
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
        if threading.activeCount() <= 2:
            self.label_03.setText("[ACTIVE CONNETCTIONS] 0")
        else:
            self.label_03.setText(f"[ACTIVE CONNETCTIONS] {threading.activeCount() - 3}")
        for connection in self.server.CONN_LIST:
            self.label_03.append(f"{connection}")
        #self.label_03.setAlignment(Qt.AlignCenter)