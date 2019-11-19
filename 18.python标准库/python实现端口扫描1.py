#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/19 23:03
# filename: python实现端口扫描1.py
from socket import *


def conn_scan(host, port):
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        conn.connect((host, port))
        print(host, port, "is avaliable")
    except Exception as e:
        print(host, port, "is not avaliable")
    finally:
        conn.close()


def main():
    host = "127.0.0.1"
    for port in range(20, 5000):
        conn_scan(host, port)

if __name__ == '__main__':
    main()

