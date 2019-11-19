#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/28 21:17
# filename: shutil操作文件.py


'''
shutil.copyfile("old", "new")     ：复制文件，old和new都是文件；
shutil.copytree("old", "new")     ：复制目录，old和new都是目录，且new必须不存在；
shutil.copy("old", "new")         ：复制文件到指定目录，new目录必须存在
shutil.move("old", "new")         ： 移动文件或目录到新的目录中，new目录可以不存在

'''

import os
import shutil

print(os.getcwd())
print(os.listdir())
shutil.copyfile("test01.txt", "test02.txt")
print(os.listdir())
shutil.copytree("dir01", "dir07")
shutil.copy("test01.txt", "dir03")
shutil.move("dir07", "dir04")
