#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
s = socket()    # 建立套接字
s.recvfrom()    #接收数据
s.sendto()      #发送数据
s.close()       #关闭套接字
'''
import socket

ip_port = ('127.0.0.1', 8888)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

data = True
while data:
    # 给服务器发送数据
    info = input(">请输入要发送的数据:")
    if not info:
        continue
    send_info = info.encode('utf-8')
    s.sendto(send_info, ip_port)
    if info == 'bye' or info == 'exit' or info == 'quit':
        print("结束通信！")
        break

    # 从服务器接收数据
    data, _ = s.recvfrom(1024)
    data = data.decode('utf-8')
    print("【服务器接收消息】:{0}".format(data))
    if data == 'bye' or data == 'exit' or data == 'quit':
        print("结束通信！")
        exit()
s.close()
