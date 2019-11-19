#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 11:35
# filename: stdin输入.py
import sys

# stdin表示流的标准输入，通过流对象stdin读取文件hello.txt的内容
sys.stdin = open("hello.txt", "r")
for line in sys.stdin.readlines():
    print(line.strip())
