#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 13:44
# filename: UDP文件上传下载Client.py


import socket

Host = '127.0.0.1'
PORT = 8888
f_name = 'test.txt'

#服务器地址
server_address = (Host, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    with open(f_name, 'r') as f:
        while True:
            data = f.read(1024)
            if data:
                #发送数据
                s.sendto(data.encode(), server_address)
            else:
                s.sendto(b'bye', server_address)

                #文件中没有可读取的数据则退出
                break

        print("客户端上传数据完成......")
