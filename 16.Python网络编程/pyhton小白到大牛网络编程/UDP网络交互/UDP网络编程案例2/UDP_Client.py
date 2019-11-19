#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/15 10:50
# filename: UDP_Client.py
import socket


def sockket_udp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostname()
    port = 9999
    for data in ['小萌', '小智']:
        # 发送数据
        s.sendto(data.encode('utf-8'), (host, port))
        # 接收数据
        print(s.recv(1024).decode('utf-8'))
    s.close()


def main():
    sockket_udp_client()


if __name__ == '__main__':
    main()
