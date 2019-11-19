#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/6 13:34
# filename: tcp_client.py

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
        self.root.title('Python在线聊天-客户端V1.0')
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
        try:
            self.clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSock.connect((self.local, self.port))
            self.flag = True
        except:
            self.flag = False
            self.chatText.insert(tkinter.END, "您还未与服务器端建立连接，请检查服务器是否启动")
            return
        self.buffer = 1024
        # 向服务器发送字符Y，表示客户端要连接服务器
        self.clientSock.send('Y'.encode())

        while True:
            try:
                if self.flag == True:
                    # 连接建立，接收服务器端消息
                    self.serverMsg = self.clientSock.recv(self.buffer).decode('utf-8')
                    if self.serverMsg == 'Y':
                        self.chatText.insert(tkinter.END, "客户端与服务器端建立连接.......")
                    elif self.serverMsg == 'N':
                        self.chatText.insert(tkinter.END, "您还未与服务器端建立连接，请检查服务器端建立连接失败..........")
                    elif not self.serverMsg:
                        continue
                    else:
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(tkinter.END, "服务器端" + theTime + '说:\n')
                        self.chatText.insert(tkinter.END, ' ' + self.serverMsg)
                else:
                    break

            except EOFError as msg:
                raise msg
                self.clientSock.close()
                break

    def sendMessage(self):
        '''
        发送消息
        :return:
        '''

        # 得到用户在Text中输入的消息
        message = self.inputText.get('1.0', tkinter.END)
        # 格式化当前的时间
        theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.chatText.insert(tkinter.END, '客户端' + theTime + "说：\n")
        self.chatText.insert(tkinter.END, ' ' + message + '\n')
        if self.flag == True:
            # 将消息发送到客户端
            self.clientSock.send(message.encode())
            self.inputText.delete(0.0, message.__len__() - 1.0)
        else:
            # Socket连接没有建立，提示用户
            self.chatText.insert(tkinter.END, '您还未与客户端建立连接，服务器端无法收到您的消息\n')
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
