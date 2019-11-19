#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/8 22:26
# filename: python逐行打印文字.py
import sys
import time


def print_one_by_one(text):
    sys.stdout.write("\r " + " " * 60 + "\r")  # /r 光标回到行首
    sys.stdout.flush()  # 把缓冲区全部输出
    # print(text)
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)


print_one_by_one("hello world my friend!")
