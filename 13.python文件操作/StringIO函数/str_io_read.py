#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/10 9:24
# filename: str_io_read.py

from io import StringIO

io_val = StringIO("Hello\nWorld\nWellcome!")
while True:
    line = io_val.readline()
    if line == '':
        break
    print("line value:{}".format(line.strip()))

"""
line value:Hello
line value:World
line value:Wellcome!
"""
