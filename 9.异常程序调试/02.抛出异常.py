#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/8 20:49
# filename: 02.抛出异常.py

try:
    raise NameError("This is NameError")  # 抛出的异常将被下面捕获
except NameError:
    print("An exception happend!")  # 捕获异常并输出，An exception happend!

try:
    raise NameError("This is NameError")  # 抛出的异常将被下面捕获
except NameError:
    print("An exception happend!")  # 捕获异常并输出，An exception happend!
    raise  # NameError: This is NameError
