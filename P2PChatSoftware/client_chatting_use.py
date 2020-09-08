from client_chatting_window import Ui_Dialog
import threading
import time
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
import socket
import json
import re
import os


class ChattingWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.udp_Socket = None  # udp_socket
        self.dest_addr = None  # 服务器的ip和端口号组成的turple
        self.name = None  # 本客户端的昵称
        self.flag = False   # 控制所有线程的循环条件
        self.current_chat_person_ip = None  # 存储客户端用户点击Table的某一行所记录的peer的name
        self.tableWidget.setColumnCount(3)  # 初始化设置Table的列表为三列
        self.tableWidget.setRowCount(5)  # 初始化设置Table的列表为五列
        self.tableWidget.setHorizontalHeaderLabels(['UserName', 'IP Address', 'Port'])  # Table的三列分别为用户名、IP地址、端口号
        self.dic = {}  # 本地存储其他peer的信息
        self.logOut_Button.clicked.connect(self.logout)  # 连接登出按钮和登出函数
        self.send_Button.clicked.connect(self.chat_with_other_peers)

    # Get命令表示向服务器请求存活的各个Peer的名称和对应的地址,客户端与服务器以Json的格式发送数据
    # 表的效果如下：
    # UserName      IP Address      Port
    #   AA          192.168.3.4     80
    #   B           124.168.5.9     3359
    #   你好        192.172.3.8     1277
    def update_member(self):
        print("更新列表")
        udp_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while self.flag:
            udp_Socket.sendto(bytes("Get", encoding="UTF-8"), self.dest_addr)
            recv_data, temp = udp_Socket.recvfrom(1000)

            if recv_data.decode("UTF-8") == "100":  #
                print("服务器已下线，列表不会再更新")
                return

            text = re.sub('\'', '\"', bytes.decode(recv_data, "UTF-8"))
            print(text)
            mydict = json.loads(text)  # ip地址 端口号 名称
            self.dic = mydict
            print(self.dic)

            index = len(mydict)

            self.tableWidget.setRowCount(0)
            self.tableWidget.clear()

            self.tableWidget.setRowCount(index)
            i = 0
            for key, value in mydict.items():
                print(value[1] + key + str(value[0]))
                self.tableWidget.setItem(i, 0, QTableWidgetItem(value[1]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(key))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(value[0])))
                i += 1
            self.tableWidget.viewport().update()
            time.sleep(5)  # 每隔5秒请求一次

    # 再设置配置的同时向服务器发送初始数据，使用的是Post方法，是对服务器端的数据进行操作，
    # 参数为1表示这是客户端对服务器进行初始化发包，服务器端会记录本机的IP地址和端口号和代号
    def setserverconfig(self, str1, str2, str3):
        self.dest_addr = (str1, int(str2))
        self.name = str3
        self.udp_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        senddata = "Post@1&"+self.name
        self.udp_Socket.sendto(senddata.encode("UTF-8"), self.dest_addr)
        recv_data, temp = self.udp_Socket.recvfrom(1000)
        recv_data = str(recv_data, "UTF-8")
        if int(recv_data) == 200:
            print("向服务器发送初始数据成功！")
        else:
            print("向服务器发送初始数据失败！")
        self.run()

    # 记录当前对话框内容，更新对话人，写入对话框
    def get_chat_person(self, row, col):

        # 当前聊天框和对话人不为空，就先记录下来
        if self.chat_record.toPlainText() != None and self.chat_record.toPlainText() != "" \
                and  self.current_chat_person_ip != None:
            name = self.dic[self.current_chat_person_ip][1]
            file_name = "chat_content_text/" + name + ".txt"
            data = self.chat_record.toPlainText()
            with open(file_name, "a") as f:
                f.write(data)
                print("已写入文件")

        self.chat_record.clear()
        self.mywords.clear()
        # 更新当前对话人
        print("第 " + str(row) + " 行" + str(col) + " 列")
        self.current_chat_person_ip = self.tableWidget.item(row, col+1).text()
        print(self.tableWidget.item(row, col).text()+self.tableWidget.item(row, col+1).text()+self.tableWidget.
              item(row, col+2).text())
        name = self.dic[self.current_chat_person_ip][1]
        print("所按按钮的值是："+name)
        file_name = "chat_content_text/"+name+".txt"
        if os.path.exists(file_name):  # 如果当前点击的peer存在与其聊天的记录就将其显示在chat_record框中
            with open(file_name, "r") as f:
                for line in f:
                    self.chat_record.append(line)

    # 在创建对象和使用setserver()函数后启动，开启三个子线程分别不断地向服务器请求实时所有的peer信息并刷新
    # 界面，另一个线程用来开启服务器功能，即不断监听来自其他peer的消息，并加以筛选
    # 第三个线程用于不断地向其他peer发送心跳包，保持内网穿透的状态
    def run(self):
        self.flag = True
        mythread = threading.Thread(target=self. update_member, args={})
        mythread.start()
        newthread = threading.Thread(target=self.run_server, args={})
        newthread.start()
        anotherthread = threading.Thread(target=self.nat_pierce, args={})
        anotherthread.start()

    # 单纯的向其他客户端发消息
    def chat_with_other_peers(self):
        print(self.current_chat_person_ip)
        target_ip = self.current_chat_person_ip
        target_port = self.dic[self.current_chat_person_ip][0]
        name = self.dic[self.current_chat_person_ip][1]
        addr = (target_ip, target_port)

        print(self.current_chat_person_ip+str(addr))

        send_data = self.mywords.toPlainText().encode("UTF-8")
        self.udp_Socket.sendto(send_data, addr)
        print("已向 " + name + " 发送信息")
        current_time = time.strftime("%Hh %Mm %Ss", time.localtime(time.time()))  # 日志信息
        # 将mywords框的信息加入chat_record框并清除mywords框信息
        self.chat_record.append("( " + current_time + " ) From" + self.name + " to " + name + ": " +
                                self.mywords.toPlainText())
        self.mywords.clear()

    # 将不同内网的peer的nat穿透，不需要无限循环的原因是他会在member_update函数的循环里面里面被调用
    # 每次更新表后就进行穿透
    def nat_pierce(self):
        #  'UserName', 'IP Address', 'Port'
        if not self.dic:  # 如果字典不为空
            send_data = "pierce".encode("UTF-8")
            for key, value in self.dic.items():
                target_ip = value[0]
                target_port = value[1]
                addr = (target_ip, target_port)
                self.udp_Socket.sendto(send_data, addr)
        time.sleep(5)

    # peer的服务器端功能将未读消息储存在本地文件中
    def run_server(self):
        server_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = socket.gethostbyname(socket.gethostname())
        port = 8080
        server_udp_socket.bind((ip, port))
        while self.flag:
            data, addr = server_udp_socket.recvfrom(1024)
            print(addr)
            name = self.dic[addr[0]][1]
            print(name)
            real_data = data.decode("UTF-8")
            print(real_data)
            if real_data == "pierce":  # 心跳包直接忽略
                return
            else:  # 其他数据则按用户名写入文件
                file_name = "chat_content_text/" + name + ".txt"
                with open(file_name, "a") as f:
                    f.write(real_data)

    # Post的方式向服务器发送请求时服务器会判断Post的参数就是@后面的数值，2代表登出，
    # 要求服务器删除对本peer的记录，回复200表示操作成功，404表示服务器未记录本机的数据
    def logout(self):
        self.udp_Socket.sendto("Post@2".encode("UTF-8"), self.dest_addr)
        recv_data, temp = self.udp_Socket.recvfrom(1000)
        recv_data = str(recv_data, "UTF-8")
        if recv_data == "{}":
            print(recv_data)
            return
        if int(recv_data) == 200 or int(recv_data) == 404:
            self.close()
        else:
            print("登出失败，服务器异常！")







