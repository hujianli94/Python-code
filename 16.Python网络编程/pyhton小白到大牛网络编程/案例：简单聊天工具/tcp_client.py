#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/7 14:16
# filename: tcp_client.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
s.connect(("127.0.0.1", 8888))

# 给服务器发送数据
s.send(b'hello')

# 从服务器接收数据
data = s.recv(1024)
print("从服务器接收数据:{}".format(data.decode()))

# 释放资源
s.close()