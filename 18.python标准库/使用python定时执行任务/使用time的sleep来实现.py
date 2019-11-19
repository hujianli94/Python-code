#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 16:27
# filename: 使用time的sleep来实现.py
import time
import os


def main(cmd, inc=60):
    while True:
        os.system(cmd)
        time.sleep(inc)


if __name__ == '__main__':
    main("netstat -an", 10)
