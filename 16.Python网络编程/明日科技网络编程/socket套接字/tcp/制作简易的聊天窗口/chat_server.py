#!/usr/bin/env python
#-*- coding:utf8 -*-
import socket
host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
sock, addr = s.accept()
print('连接已经建立')
info = sock.recv(1024).decode()

while info != 'byebye':
    if info:
        print("接收到的内容: %s " % info)
    send_data = input("输入发送的内容: ")
    sock.send(send_data.encode())
    if send_data == "byebye":
        break
    info = sock.recv(1024).decode()

sock.close()
s.close()