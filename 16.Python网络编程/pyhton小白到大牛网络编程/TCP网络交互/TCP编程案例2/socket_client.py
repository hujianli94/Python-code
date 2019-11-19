#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/15 10:38
# filename: socket_client.py
import socket

def socket_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.connect((host, port))

    # 接收欢迎消息
    print(s.recv(1024).decode('utf-8'))
    for data in ['小智', '小萌', '小强']:
        # 发送数据
        s.send(data.encode('utf-8'))
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()


def main():
    socket_client()


if __name__ == '__main__':
    main()
