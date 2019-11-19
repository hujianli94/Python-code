#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
s = socket()        #建立套接字
s.bind()            #绑定本机地址
s.recvfrom()        #接收数据
s.sendto()          #发送数据
s.close()           #关闭套接字
'''

import socket

ip_port = ('', 8888)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.bind(ip_port)
print("服务器启动.......")
data = True
while data:
    data, client_address = s.recvfrom(1024)
    data = data.decode('utf-8')
    if data == 'bye' or data == 'exit' or data == 'quit':
        print("结束通信！")
        break
    print("【客户端接收消息】：{0}".format(data))

    while True:
        # 给客户端发送消息
        info = input(">请输入要发送的信息:").strip()
        if not info:
            continue
        elif info == 'bye' or info == 'exit' or info == 'quit':
            send_info = info.encode('utf-8')
            s.sendto(send_info, client_address)
            print("结束通信！")
            exit()
        else:
            send_info = info.encode('utf-8')
            s.sendto(send_info, client_address)
            break
s.close()
