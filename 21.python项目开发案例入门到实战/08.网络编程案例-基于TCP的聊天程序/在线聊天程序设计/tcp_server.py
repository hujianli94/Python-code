#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/6 11:35
# filename: tcp_server.py
import tkinter
import tkinter.font as tkFont
import socket
import threading
import sys
import time


class ServerUI():
    local = "127.0.0.1"
    port = 5505
    global serverSock
    flag = False

    def __init__(self):
        '''
        初始类相关属性的构造函数
        '''
        self.root = tkinter.Tk()
        self.root.title('Python在线聊天-服务器V1.0')
        # 窗口面板，用4个frame面板布局
        self.frame = [tkinter.Frame(), tkinter.Frame(), tkinter.Frame(), tkinter.Frame()]
        # 显示消息Text右边的滚动条
        self.chatTextScrollBar = tkinter.Scrollbar(self.frame[0])
        self.chatTextScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # 显示消息Text，并绑定上面的滚动条
        ft = tkFont.Font(family='Fixdsys', size=11)
        self.chatText = tkinter.Listbox(self.frame[0], width=70, height=18, font=ft)
        self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
        self.chatText.pack(expand=1, fill=tkinter.BOTH)
        self.chatTextScrollBar['command'] = self.chatText.yview()
        self.frame[0].pack(expand=1, fill=tkinter.BOTH)

        # 输入消息Text的滚动条
        self.inputTextScrollBar = tkinter.Scrollbar(self.frame[2])
        self.inputTextScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # 输入消息Text，并与滚动条绑定
        ft = tkFont.Font(family='Fixdsys', size=11)
        self.inputText = tkinter.Text(self.frame[2], width=70, height=8, font=ft)
        self.inputText['yscrollcommand'] = self.inputTextScrollBar.set
        self.inputText.pack(expand=1, fill=tkinter.BOTH)
        self.inputTextScrollBar['command'] = self.chatText.yview()
        self.frame[2].pack(expand=1, fill=tkinter.BOTH)

        # “发送”按钮
        self.sendButton = tkinter.Button(self.frame[3], text="发送", width=10, command=self.sendMessage)
        self.sendButton.pack(expand=1, side=tkinter.Button and tkinter.RIGHT, padx=25, pady=5)

        # “关闭”按钮
        self.closeButton = tkinter.Button(self.frame[3], text="关闭", width=10, command=self.close)
        self.closeButton.pack(expand=1, side=tkinter.RIGHT, padx=25, pady=5)
        self.frame[3].pack(expand=1, fill=tkinter.BOTH)

    def receiveMessage(self):
        """
        接收消息
        """
        # 建立Socket连接
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSock.bind((self.local, self.port))
        self.serverSock.listen(15)
        self.buffer = 1024
        self.chatText.insert(tkinter.END, "服务器已经就绪............")

        # 循环接受客户端的连接请求
        while True:
            self.connection, self.address = self.serverSock.accept()
            self.flag = True
            while True:
                # 接收客户端发送的消息
                self.cientMsg = self.connection.recv(self.buffer).decode('utf-8')
                if not self.cientMsg:
                    continue
                elif self.cientMsg == 'Y':
                    self.chatText.insert(tkinter.END, '服务器已经与客户端建立连接.......')
                    self.connection.send(b'Y')
                elif self.cientMsg == 'N':
                    self.chatText.insert(tkinter.END, '服务器与客户端建立连接失败...........')
                    self.connection.send(b'N')
                else:
                    theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    self.chatText.insert(tkinter.END, '客户端' + theTime + '说：\n')
                    self.chatText.insert(tkinter.END, ' ' + self.cientMsg)

    def sendMessage(self):
        '''
        发送消息
        :return:
        '''

        # 得到用户在Text中输入的消息
        message = self.inputText.get('1.0', tkinter.END)
        # 格式化当前的时间
        theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.chatText.insert(tkinter.END, '服务器' + theTime + "说：\n")
        self.chatText.insert(tkinter.END, ' ' + message + '\n')
        if self.flag == True:
            # 将消息发送到客户端
            self.connection.send(message.encode())
            self.inputText.delete(0.0, message.__len__() - 1.0)

        else:
            # Socket连接没有建立，提示用户
            self.chatText.insert(tkinter.END, '您还未与客户端建立连接，客户端无法收到您的消息\n')
            # 清空用户在Text中输入的消息
            self.inputText.delete(0.0, message.__len__() - 1.0)

    def close(self):
        '''
        关闭消息窗口并退出
        :return:
        '''
        sys.exit()


    def startNewThread(self):
        '''
        启动一个新线程来接收客户端的消息
        :return:
        '''
        thread = threading.Thread(target=self.receiveMessage, args=())
        thread.setDaemon(True)
        thread.start()


def main():
    server = ServerUI()
    server.startNewThread()
    server.root.mainloop()


if __name__ == '__main__':
    main()
