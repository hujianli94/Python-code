#!/usr/bin/env python
#-*- coding:utf8 -*-
import socket
host = socket.gethostname()
# port = 12345
port = 60000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print('已经连接')

info = ''
while info != 'byebye':
    send_data = input("输入发送内容：")
    s.send(send_data.encode('gbk'))
    if send_data == 'byebye':
        break
    info = s.recv(1024).decode('gbk')
    print('接收到的内容：%s' % info)