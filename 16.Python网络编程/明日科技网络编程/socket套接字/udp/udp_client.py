#!/usr/bin/env python
#-*- coding:utf8 -*-
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = input("请输入要转化的温度（单位：摄氏度）: ")
s.sendto(data.encode(),("127.0.0.1",8888))
print("转化后的华氏度{}".format(s.recv(1024).decode()))
s.close()