#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 11:39
# filename: stdout输出到文件中.py
import sys


# 通过stdout对象重定向输出，把输出的结果保存到文件中
sys.stdout = open(r"./hello.txt", "a")
print("goodbye")
sys.stdout.close()
