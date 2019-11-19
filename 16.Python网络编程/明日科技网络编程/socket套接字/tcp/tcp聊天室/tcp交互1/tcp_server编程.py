#!/usr/bin/env python
# -*- coding:utf8 -*-
import socket

host = '127.0.0.1'
port = 10888

web = socket.socket()  # 定义socket对象
web.bind((host, port))  # 开始监听
web.listen(5)  # 最大监听数量
print("服务器等待客户端连接....")
while True:
    conn, addr = web.accept()
    data = conn.recv(1024)  # 最大接收数据
    print(data.decode('utf-8'))
    conn.sendall(b'Status Code: 200 OK! \r\n\r\nhello world ')
    conn.close()
