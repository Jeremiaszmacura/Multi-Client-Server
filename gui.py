# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_01.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(308, 281)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.on_off_button = QtWidgets.QPushButton(self.centralwidget)
        self.on_off_button.setGeometry(QtCore.QRect(50, 110, 81, 81))
        self.on_off_button.setObjectName("on_off_button")
        self.on_off_img = QtWidgets.QLabel(self.centralwidget)
        self.on_off_img.setGeometry(QtCore.QRect(170, 130, 81, 51))
        self.on_off_img.setText("")
        self.on_off_img.setPixmap(QtGui.QPixmap("assets/icons8-toggle-off-80.png"))
        self.on_off_img.setObjectName("on_off_img")
        self.label_server = QtWidgets.QLabel(self.centralwidget)
        self.label_server.setGeometry(QtCore.QRect(110, 10, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_server.setFont(font)
        self.label_server.setObjectName("label_server")
        self.on_off_info = QtWidgets.QLabel(self.centralwidget)
        self.on_off_info.setGeometry(QtCore.QRect(200, 180, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.on_off_info.setFont(font)
        self.on_off_info.setObjectName("on_off_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 21))
        self.menubar.setObjectName("menubar")
        self.menuServer = QtWidgets.QMenu(self.menubar)
        self.menuServer.setObjectName("menuServer")
        self.menuClient = QtWidgets.QMenu(self.menubar)
        self.menuClient.setObjectName("menuClient")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuServer.menuAction())
        self.menubar.addAction(self.menuClient.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.on_off_button.clicked.connect(self.show_img_server_on)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.on_off_button.setText(_translate("MainWindow", "PushButton"))
        self.label_server.setText(_translate("MainWindow", "Server"))
        self.on_off_info.setText(_translate("MainWindow", "OFF"))
        self.menuServer.setTitle(_translate("MainWindow", "Server"))
        self.menuClient.setTitle(_translate("MainWindow", "Client"))

    def show_img_server_on(self):
        self.on_off_img.setPixmap(QtGui.QPixmap("assets/icons8-toggle-on-80.png"))
        _translate = QtCore.QCoreApplication.translate
        self.on_off_info.setText(_translate("MainWindow", "ON"))

    def show_img_server_off(self):
        self.on_off_img.setPixmap(QtGui.QPixmap("assets/icons8-toggle-off-80.png"))
        _translate = QtCore.QCoreApplication.translate
        self.on_off_info.setText(_translate("MainWindow", "OFF"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
