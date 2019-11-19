#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/15 10:45
# filename: UDP_Server.py
import socket


def socket_udp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostname()
    port = 9999
    # 绑定端口
    s.bind((host, port))

    while True:
        # 接收数据
        data, addr = s.recvfrom(1024)
        print("Received from {}".format(addr))
        s.sendto(b"hello,%s,welcome!" % data, addr)


def main():
    socket_udp_server()


if __name__ == '__main__':
    main()
