#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
filename ="hujianli.txt.bak"

## 创建一个硬链接文件
os.link(filename,"hujianli.txt")

print(os.path.isfile("hujianli.txt"))


## 创建一个符号链接（软链接）
os.symlink("hujianli.txt", "hujianli2.txt")