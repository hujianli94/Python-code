#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 13:24
# filename: TCP文件上传工具Client.py
import socket

Host = '127.0.0.1'
PORT = 8888
f_name = 'coco2dxcplus_copy.jpg'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, PORT))
    with open(f_name, 'rb') as f:
        b = f.read()
        s.sendall(b)
        print("客户端上传数据完成........")
