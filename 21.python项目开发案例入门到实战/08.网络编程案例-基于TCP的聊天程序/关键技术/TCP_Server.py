#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/6 10:36
# filename: TCP_Server.py
import socket
import threading
import time


def tcplink(sock, addr):
    print("【接收一个来自{}:{}连接请求】".format(addr[0], addr[1]))
    # 发给客户端Welcom！信息
    a = "Wellcome!"
    sock.send(a.encode())
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,{}!'.format(data.decode('utf-8')).encode('utf-8')))

    sock.close()
    print("【来自{}:{}连接关闭了】".format(addr[0], addr[1]))


# 创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听本机8888端口
s.bind(('127.0.0.1', 8888))
# 连接的最大数量为5
s.listen(5)
print("等待客户端连接.....")

while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
