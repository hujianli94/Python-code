#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/17 12:43
# filename: check_port.py
import socket


def check_server(address, port=80):
    s = socket.socket()
    print('Attempting to connect to %s on port %s' % (address, port))
    try:
        s.connect((address, port))
        print('Connected to %s on port %s' % (address, port))
        return True
    except socket.error as e:
        print('Connection to %s on port %s failed: %s' % (address, port, e))
        return False
    finally:
        s.close()


check_server("220.181.111.37")
