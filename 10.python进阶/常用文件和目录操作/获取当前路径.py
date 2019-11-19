#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
#获取当前的目录
print("当前目录是:{}".format(os.getcwd()))


#获取目录中的内容
print("目录中的内容有：{}".format(os.listdir()))


#创建目录
if not os.path.exists("test_hu"):
    print("开始创建目录.....test_hu")
    os.mkdir("test_hu")
else:
    print("目录中的内容有：{}".format(os.listdir()))

#删除目录
print("开始删除目录......test_hu",)
os.rmdir("test_hu")
print("目录中的内容有：{}".format(os.listdir()))

os.mkdir("test_hu")
#判断是否是目录
print("判断是否是目录？")
print(os.path.isdir("test_hu"))
print(os.path.isdir("fab.txt"))

#判断是否是文件
print("判断是否为文件?")
with open("fab1.txt","w+") as f:
    f.write("hello this is file test")
print(os.path.isfile("fab1.txt"))
print(os.path.isfile("test_hu"))





