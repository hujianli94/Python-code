#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
filename = "hujianli.txt"
##检查是否是文件
print(os.path.isfile(filename))
## 检查是否是目录
print(os.path.isdir(filename))

## 检查是否是绝对路径
print(os.path.isabs("/home/rzrk/hujianli.txt"))
print(os.path.isabs("../hujianli.txt"))

