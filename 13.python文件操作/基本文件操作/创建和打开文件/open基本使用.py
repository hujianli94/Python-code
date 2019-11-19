#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/27 10:05
# filename: open基本使用.py

try:
    f = open("message.txt", "r")
    print(f.read())
finally:
    if f:
        f.close()
