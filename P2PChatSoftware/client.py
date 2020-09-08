# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from rescource import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(235, 246)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/images/windowIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget:window{\n"
"    border-image: url(:/image/images/bg1.jpg);\n"
"}\n"
"QLineEdit{\n"
"    border:2px groove #FF4500;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"    color:#FF4500\n"
"}\n"
"QPushButton{\n"
"    border:2px groove #8B008B;\n"
"    border-radius:6px;\n"
"    padding:5px 4px\n"
"}\n"
"QPushButton:hover{\n"
"     background-color:rgb(0,0,0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(255,255,255);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"QLabel{\n"
"    border:5px groove #000000;\n"
"    border-radius:5px;\n"
"    padding:3px 4px;\n"
"    border:none;\n"
"    font: 14pt \"楷体\";\n"
"    color:#FF4500;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(100, 180, 51, 41))
        self.startButton.setStyleSheet("border-image: url(:/image/images/start.ico);")
        self.startButton.setText("")
        self.startButton.setObjectName("startButton")
        self.name_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_LineEdit.setGeometry(QtCore.QRect(60, 120, 131, 41))
        self.name_LineEdit.setStyleSheet("font: 12pt \"华文楷体\";")
        self.name_LineEdit.setObjectName("name_LineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 91))
        self.label.setStyleSheet("border-image: url(:/image/images/client.png);\n"
"background-color:rgb(0,0,0,0)")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionsettings = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionsettings.setFont(font)
        self.actionsettings.setPriority(QtWidgets.QAction.HighPriority)
        self.actionsettings.setObjectName("actionsettings")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.name_LineEdit.setPlaceholderText(_translate("MainWindow", "输入聊天昵称"))
        self.actionsettings.setText(_translate("MainWindow", "settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

