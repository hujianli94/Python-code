#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/24 9:22
# filename: TCPserver.py
import socket
ip_port = ('127.0.0.1', 9999)

sk = socket.socket()            # 创建套接字
sk.bind(ip_port)                # 绑定服务地址
sk.listen(5)                    # 监听连接请求
print('启动socket服务，等待客户端连接...')
conn, address = sk.accept()     # 等待连接，此处自动阻塞
while True:     # 一个死循环，直到客户端发送‘exit’的信号，才关闭连接
    client_data = conn.recv(1024).decode()      # 接收信息
    if client_data == "exit":       # 判断是否退出连接
        print("结束通信！")
        break
    print("【来自%s的客户端向你发来信息】：%s" % (address, client_data))
    send_input = input(">请输入要发送的内容：")
    conn.send(send_input.encode())
    if send_input == "exit":
        print("结束通信！")
        break
conn.close()    # 关闭连接