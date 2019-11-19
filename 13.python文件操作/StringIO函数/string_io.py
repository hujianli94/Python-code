#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/10 9:22
# filename: string_io.py
from io import StringIO

io_val = StringIO()
io_val.write("hello")

# getvalue()方法用于获得写入后的str
print("say:{}".format(io_val.getvalue()))

"""
say:hello
"""


