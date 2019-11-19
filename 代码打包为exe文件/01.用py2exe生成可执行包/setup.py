#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 16:56
# filename: setup.py
from distutils.core import setup
import py2exe

setup(console=['hello.py'])  # 指定为控制台程序的主程序文件名
# setup(windows=['hello.py'])     #编译成GUI的可执行文件
