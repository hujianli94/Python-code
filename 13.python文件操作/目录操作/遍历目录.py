#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
#os.walk(top, topdown=True, onerror=None, followlinks=False)
'''
   dirpath, dirnames, filenames

    dirpath is a string, the path to the directory.
    dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..').
    filenames is a list of the names of the non-directory files in dirpath.
'''
path = r"D:\Cisco_iso"
print("【", path, "】目录下包含的文件和目录：")

for root,dirs,files in os.walk(path,topdown=True):  #遍历指定目录
    for name in dirs:
        print(os.path.join(root, name))      #输出遍历到的目录
    for name in files:
        print('\t', os.path.join(root, name))      #输出遍历到的文件