#!/usr/bin/env python
# -*- coding:utf8 -*-
import socket

host = '127.0.0.1'
port = 10888

client = socket.socket()  # 定义socket对象
client.connect((host, port))
send_data = input("请输入要发送的数据：")
client.send(send_data.encode())
recv_data = client.recv(1024)
print("接收到的数据是:%s " % recv_data.decode('utf-8'))
client.close()
