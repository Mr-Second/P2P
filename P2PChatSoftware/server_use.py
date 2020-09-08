from server import Ui_Dialog
import socket
from copy import deepcopy
import time
import threading
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem


class Server(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.port = 8080
        self.ip_address = socket.gethostbyname(socket.gethostname())
        self.setWindowTitle("Server")
        self.socket = None

        print("服务器IP地址为："+self.ip_address)
        self.user_ip_dict = {}  # 用户名与IP地址和端口号对应列表
        self.flag = False  # 用于控制服务器的启动与关闭
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['IP Address', 'Port', 'UserName'])
        self.beginButton.clicked.connect(self.run)
        self.stopButton.clicked.connect(self.exit)

    def run(self):
        self.beginButton.setEnabled(False)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_address, self.port))
        newthread = threading.Thread(target=self.listen_from_client)
        self.flag = True
        newthread.start()
        self.logArea.appendPlainText("服务器已启动！")

    def listen_from_client(self):
        self.logArea.appendPlainText("对客户端的监听开始。。。")
        while self.flag:
            data, addr = self.socket.recvfrom(1024)
            data = str(data, "UTF-8")  # 将字节数组转换为字符串
            if data.find("Get") != -1:  # 如果获取的是Get请求
                send_data = str(self.user_ip_dict).encode("UTF-8")  # 先将字典转换为字符串在转换为字节数组
                self.socket.sendto(send_data, addr)
                continue
            elif data.find("Post") != -1:  # 如果获取的是Post,再判断指令参数
                pos = data.find("Post")
                pos += 5
                if data[pos] == "1":  # 指令参数为1
                    name = data.split("&")[1]  # 获取peer的name
                    self.user_ip_dict[addr[0]] = [addr[1], name]  # IP地址对应端口号和名称
                    send_data = "200".encode("UTF-8")
                    self.socket.sendto(send_data, addr)
                    self.update_information("IP地址为 "+addr[0]+" 的 "+name+" 已上线")
                    self.flood()
                    continue
                elif data[pos] == "2":
                    if self.user_ip_dict.get(addr[0]):
                        print(self.user_ip_dict)
                        values = self.user_ip_dict.get(addr[0])
                        ip = addr[0]
                        del self.user_ip_dict[addr[0]]  # 存在则删除该peer的信息
                        print(self.user_ip_dict)
                        send_data = "200".encode("UTF-8")
                        self.socket.sendto(send_data, addr)
                        self.update_information("IP地址为 " + ip + " 的 "+values[1]+" 已下线")
                        self.flood()
                        continue
                    else:
                        send_data = "404".encode("UTF-8")
                        self.socket.sendto(send_data, addr)
                        continue

    # 每次服务器的记录信息更新后都会向所有peer发送更新消息
    def flood(self):
        # self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.socket.bind((self.ip_address, self.port))
        for key, value in self.user_ip_dict.items():
            tempidct = deepcopy(self.user_ip_dict)  # 深拷贝
            addr = (key, int(value[0]))
            print(key, int(value[0]))
            del tempidct[key]   # 删除该peer的IP信息发送其他的peer的信息给它
            send_data = str(tempidct).encode("UTF-8")
            self.socket.sendto(send_data, addr)

    # 更新界面
    def update_information(self, information):
        i = 0
        self.tableWidget.clearContents()
        for key, value in self.user_ip_dict.items():
            a = QTableWidgetItem(key)
            b = QTableWidgetItem(str(value[0]))
            c = QTableWidgetItem(value[1])
            self.tableWidget.setItem(i, 0, a)
            self.tableWidget.setItem(i, 1, b)
            self.tableWidget.setItem(i, 2, c)
            i += 1
        self.tableWidget.viewport().update()
        current_time = time.strftime("%Hh %Mm %Ss",time.localtime(time.time()))  # 日志信息
        self.logArea.appendPlainText(current_time + ": "+str(information))

    def exit(self):
        self.flag = False
        # self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.socket.bind((self.ip_address, self.port))
        for key, value in self.user_ip_dict.items():
            addr = (key, value[0])
            send_data = "100".encode("UTF-8")
            self.socket.sendto(send_data, addr)
        self.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Server(Dialog)
    ui.exec_()
    sys.exit(app.exec_())
