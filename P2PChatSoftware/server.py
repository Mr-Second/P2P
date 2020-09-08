# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from rescource import images_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(339, 435)
        Dialog.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 321, 411))
        self.frame.setStyleSheet("\n"
"background-color: rgb(255, 255, 255，0);\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 1, 321, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 12pt \"华文楷体\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setStyleSheet("font: 12pt \"华文楷体\";\n"
"color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 12pt \"华文楷体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.logArea = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.logArea.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 11pt \"华文楷体\";")
        self.logArea.setReadOnly(True)
        self.logArea.setPlainText("")
        self.logArea.setObjectName("logArea")
        self.verticalLayout.addWidget(self.logArea)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 3)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 350, 111, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stopButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 40))
        self.stopButton.setStyleSheet("QPushButton{\n"
"    \n"
"    border-image: url(:/image/images/stop.png);\n"
"}\n"
"QPushButton::hover{  \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  \n"
"                                 stop: 0 #758385, stop: 0.5 #122C39,  \n"
"                                 stop: 1.0 #0E7788);  \n"
"    border-color: #11505C;  \n"
"\n"
"}  \n"
"QPushButton::pressed{  \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  \n"
"                                 stop: 0 #969B9C, stop: 0.5 #16354B,  \n"
"                                 stop: 1.0 #244F76);  \n"
"    border-color: #11505C;\n"
"\n"
"} ")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 0, 1, 1, 1)
        self.beginButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.beginButton.setMinimumSize(QtCore.QSize(0, 40))
        self.beginButton.setStyleSheet("QPushButton{\n"
"border-image: url(:/image/images/begin.ico);\n"
"}\n"
"QPushButton::hover{  \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  \n"
"                                 stop: 0 #758385, stop: 0.5 #122C39,  \n"
"                                 stop: 1.0 #0E7788);  \n"
"    border-color: #11505C;  \n"
"\n"
"}  \n"
"QPushButton::pressed{  \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  \n"
"                                 stop: 0 #969B9C, stop: 0.5 #16354B,  \n"
"                                 stop: 1.0 #244F76);  \n"
"    border-color: #11505C;\n"
"\n"
"} ")
        self.beginButton.setText("")
        self.beginButton.setObjectName("beginButton")
        self.gridLayout.addWidget(self.beginButton, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Peer信息"))
        self.label.setText(_translate("Dialog", "日志信息"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

