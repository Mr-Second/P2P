from client import Ui_MainWindow
import threading
# from  client_chatting_window import Ui_Dialog
from client_chatting_use import ChattingWindow
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, \
                            QMainWindow, QApplication, \
                            QPushButton, QMessageBox


class Client(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(239, 246)
        self.name = None
        self.startButton.clicked.connect(self.on_button_start_clicked)

    # 动态创建一个对话框，让用户配置服务器的IP地址和端口号
    def on_button_start_clicked(self):
        if self.name_LineEdit.text():
            self.name = self.name_LineEdit.text()
            print("昵称为："+self.name)
        else:
            QMessageBox.warning(self, "警告！", "昵称不能为空！", QMessageBox.Ok)
            return
        inputDialog = QDialog()
        inputDialog.setFixedSize(200, 200)
        inputDialog.setWindowTitle("配置框")

        inputDialog.ip_inputLine = QLineEdit()
        inputDialog.ip_inputLine.setFixedSize(120, 30)
        inputDialog.ip_inputLine.move(63, 50)
        inputDialog.ip_inputLine.setParent(inputDialog)
        inputDialog.ip_inputLine.show()

        inputDialog.port_inputLine = QLineEdit()
        inputDialog.port_inputLine.setFixedSize(120, 30)
        inputDialog.port_inputLine.move(63, 90)
        inputDialog.port_inputLine.setParent(inputDialog)
        inputDialog.port_inputLine.show()

        inputDialog.ipLabel = QLabel()
        inputDialog.portLabel = QLabel()
        inputDialog.ipLabel.setFixedSize(61, 31)
        inputDialog.ipLabel.move(0, 50)
        inputDialog.portLabel.setFixedSize(61, 31)
        inputDialog.portLabel.move(0, 90)
        inputDialog.ipLabel.setText("IP Address")
        inputDialog.portLabel.setText("Port")
        inputDialog.ipLabel.setParent(inputDialog)
        inputDialog.portLabel.setParent(inputDialog)
        inputDialog.ipLabel.show()
        inputDialog.portLabel.show()

        inputDialog.confirmButton = QPushButton()
        inputDialog.confirmButton.setText("Confirm")
        inputDialog.confirmButton.setFixedSize(75, 23)
        inputDialog.confirmButton.move(85, 140)
        inputDialog.confirmButton.setParent(inputDialog)
        inputDialog.confirmButton.show()

        inputDialog.confirmButton.clicked.connect(inputDialog.close)

        inputDialog.confirmButton.clicked.connect(lambda: self.on_dailog_confirm_button_clicked
        (inputDialog.ip_inputLine.text(), inputDialog.port_inputLine.text()))

        inputDialog.exec_()

    # 获取服务器端口和端口号等配置
    def on_dailog_confirm_button_clicked(self, str1, str2):
        if str1 and str2 and len(str1.split(".")) == 4:

            print("服务器IP地址为： "+str1+" 服务器端的端口为："+str2)

            tempChattingDailog = ChattingWindow()
            tempChattingDailog.setserverconfig(str1, str2, self.name)
            self.close()
            tempChattingDailog.exec_()
        else:
            QMessageBox.warning(self, "警告！", "服务器IP地址或端口号为空或IP地址格式错误", QMessageBox.Yes)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = Client()
    mainWindow.show()
    sys.exit(app.exec_())
