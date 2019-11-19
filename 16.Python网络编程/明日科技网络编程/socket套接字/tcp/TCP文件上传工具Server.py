#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 13:16
# filename: TCP文件上传工具Server.py
import socket

HOST = ''
PORT = 8888

f_name = 'coco2dxcplu_copy1.jpg'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    print("服务器启动.........")

    while True:
        with s.accept()[0] as conn:
            # 创建字节序列对象列表，作为接受数据的缓冲区
            buffer = []
            while True:
                data = conn.recv(1024)
                if data:
                    # 接收的数据添加到缓冲区
                    buffer.append(data)
                else:
                    # 没有接收到数据则退出
                    break
            b = bytes().join(buffer)        #将buffer中的字节连接合并为一字节序列对象，bytes()是创建一个空的字节序列对象
            with open(f_name, "wb") as f:
                f.write(b)

            print("服务器接收完成。")