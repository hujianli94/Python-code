#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 13:39
# filename: UDP文件上传下载Server.py

import socket

HOST = '127.0.0.1'
PORT = 8888

f_name = 'test_copy2.txt'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("服务器启动.........")

    # 创建字节序列对象列表，作为接受数据的缓冲区
    buffer = []
    while True:         #反复接收数据
            data, _ = s.recvfrom(1024)
            if data:
                # 接收的数据添加到缓冲区
                flag = data.decode()
                if flag == "bye":
                    break
                buffer.append(data)
            else:
                #没有接收到数据，进入下次循环继续接收
                continue

            # 将buffer中的字节连接合并为一字节序列对象，bytes()是创建一个空的字节序列对象
            b = bytes().join(buffer)
            with open(f_name, "w") as f:
                f.write(b.decode())

            print("服务器接收完成。")