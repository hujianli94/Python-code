#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
'''
scr = r"D:\\deam\\aaa.txt"      #原路径
dst = r"D:\\deam\\aaa22.txt"    #修改后

if os.path.exists(scr):
    os.rename(scr, dst)         #重名了文件
else:
    print("目录不存在")

'''
scr = r"D:\\deam"      #原路径
dst = r"D:\\deam1"    #修改后

if os.path.exists(scr):
    os.rename(scr, dst)         #重名了文件
else:
    print("目录不存在")