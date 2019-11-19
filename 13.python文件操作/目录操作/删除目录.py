#!/usr/bin/env python
#-*- coding:utf8 -*-
#删除目录
import os,shutil
'''
if os.path.exists("D:\deam\\test\\aaa"):
    os.rmdir("D:\deam\\test\\aaa")
else:
    print("目录不存在！！！")

if os.path.exists("D:\deam\\test\\bbb"):
    os.rmdir("D:\deam\\test\\bbb")
else:
    print("目录不存在！！！")

if os.path.exists("D:\deam"):
    os.rmdir("D:\\deam")
else:
    print("目录不存在！！！")
'''
path = "D:\deam"
aaa_path = "D:\deam\\test\\aaa"
bbb_path = "D:\deam\\test\\bbb"
if os.path.exists(aaa_path):
    shutil.rmtree("D:\deam\\test\\aaa")
else:
    print("目录不存在！！！")

shutil.rmtree(path)