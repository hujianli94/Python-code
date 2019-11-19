#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/21 10:23
# filename: socket实现端口扫描.py
import socket
import threading
import time


def testconn(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((host, port))
        return host + " Server is " + str(port) + " connect"
    except Exception:
        return host + " Server is " + str(port) + " not connect!"
    sk.close()


class Test(threading.Thread):
    def __init__(self):
        pass

    def test(self):
        test_conn = testconn('127.0.0.1', 80)
        print(test_conn)
    def run(self):
        while True:
            # print time.strftime('%Y-%m-%d %H:%M:%S')
            self.test()
            time.sleep(1)


a = Test()
a.run()
