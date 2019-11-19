#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/1 9:33
# filename: 格式化字符串可用格式字符.py
import struct

a = 20
bytes2 = struct.pack("i", a)  # 将a变为字符串
print(bytes2)

a = "hello"
b = "world!"
c = 2
d = 45.123

bytes = struct.pack("5s6sif", a.encode("utf-8"), b.encode("utf-8"), c, d)
print(bytes)

binfile = open("hellobin.txt", "ab")
binfile.write(bytes)
binfile.close()


