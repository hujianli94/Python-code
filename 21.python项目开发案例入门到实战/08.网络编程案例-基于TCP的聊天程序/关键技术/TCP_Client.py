#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/6 10:44
# filename: TCP_Client.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))  # 建立连接

# 打印接收到欢迎消息
print(s.recv(1024).decode('utf-8'))

# 客户端程序发送人名数据给服务端
list_name = ["a", "b", "c", "d", "e", "Michael", "Tracy", "Sarah"]
for data in list_name:
    s.send(data.encode())
    print(s.recv(1024).decode('utf-8'))
