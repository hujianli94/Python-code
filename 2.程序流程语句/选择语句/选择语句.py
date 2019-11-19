#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
简单的if语句
if 表达式：（布尔值）
    语句块


if 表达式:
   语句块1
else:
    语句块2


if 表达式:
    语句块1
elif 表达式:
    语句块2
else:
    语句块3


#推荐写法
if flag:
    pass

if not flag:
    pass


if a == 1:
    pass


########################if 的嵌套方式########################
if 表达式1：
    if 表达式2：
        语句块2
    else:
        语句块3
else:
    语句块1
"""

has_y = False

suffix = "hujianli.py"
suffix = "." + suffix.split(".")[1]

if suffix == ".htm":
    has_y = True
elif suffix == ".py":
    has_y = True
elif suffix == ".sh":
    has_y = True
elif suffix == ".png" or suffix == ".jpg":
    has_y = True
else:
    raise RuntimeError("Unknow content type.")

print(has_y)