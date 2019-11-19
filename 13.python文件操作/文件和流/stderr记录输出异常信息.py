#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 11:42
# filename: stderr记录输出异常信息.py
import sys
import time

sys.stderr = open("error.log", "a", encoding="utf-8")
f = open(r"./hello.txt", "r")
t = time.strftime("%Y-%m-%d %X", time.localtime())
context = f.read()
if context:
    sys.stderr.write(t + " " + context)
else:
    raise Exception(t + ' 异常信息')
