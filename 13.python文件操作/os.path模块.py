#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/6 16:25
# filename: os.path模块.py
import os.path
from datetime import datetime

f_name = "test.txt"
af_name = r"D:\GitHub\21_staduy_python\9.1.python文件操作\foo_bak.txt"

#返回路径中基础名部分
basename = os.path.basename(af_name)
print(basename)

#返回路径中的目录部分
dirname = os.path.dirname(af_name)
print(dirname)

#返回文件的绝对路径
abs_path = os.path.abspath(af_name)
print(abs_path)

#返回文件的大小
print("{0}: {1}KB".format(os.path.basename(af_name), os.path.getsize(af_name)))

#返回文件的创建时间
ctime = datetime.fromtimestamp(os.path.getctime(af_name))
print(ctime)

#返回文件修改时间
mtime = datetime.fromtimestamp(os.path.getmtime(af_name))
print(mtime)

print(os.path.isfile(dirname))
print(os.path.isdir(dirname))
print(os.path.isfile(f_name))
print(os.path.isdir(f_name))
print(os.path.exists(f_name))