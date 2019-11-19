#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 17:33
# filename: 01.实现SSH自动登录示例.py
from pexpect import pxssh


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print(s.before)


def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print("error")
        exit(0)


def main():
    s = connect('192.168.0.100', 'root', 'admin#123')
    send_command(s, 'whoami')


if __name__ == '__main__':
    main()