#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/19 23:10
# filename: python使用telnet模块检测端口.py
import telnetlib


def conn_scan(host, port):
    t = telnetlib.Telnet()
    try:
        t.open(host, port, timeout=1)
        print(host, port, "is avaliable")
    except Exception as e:
        print(host, port, "is not avaliable")
    finally:
        t.close()


def main():
    host = "127.0.0.1"
    for port in range(80, 5000):
        conn_scan(host, port)


if __name__ == '__main__':
    main()
