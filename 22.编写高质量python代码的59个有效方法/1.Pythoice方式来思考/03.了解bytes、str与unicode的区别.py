#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 11:59
# filename: 03.了解bytes、str与unicode的区别.py
"""
python3的str实例和python2的unicode实例都没有和特定的二进制编码形式相关联，
要想把Unicode字符转换成二进制数据，就必须使用encode方法。
要想把二进制数据转成Unicode字符，则必须使用decode方法。
"""


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # 返回字符串


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value  # 返回bytes


import os

with open("random.bin", "wb") as f:
    f.write(os.urandom(10))
