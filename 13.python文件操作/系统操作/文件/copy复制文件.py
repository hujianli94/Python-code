#!/usr/bin/env python
#-*- coding:utf8 -*-
import shutil
filename = "hujianli.txt"
shutil.copy(filename, filename +".bak")

## 改名文件
shutil.move(filename,filename + "remove.bak")