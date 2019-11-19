#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 11:29
# filename: 读取二进制并显示.py
import struct

# # 字符串还原成数据
bytes = struct.pack("i", 20)
a, = struct.unpack("i", bytes)
print(a)
bytes = struct.pack("i", a)
a, = struct.unpack("i", bytes)
# (a,) = struct.unpack("i", bytes)


with open("hellobin.txt", "rb") as f:
    bytes = f.read()
    t = struct.unpack('5s6sif', bytes)

print(t)
