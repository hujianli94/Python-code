#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
#os.mkdir(path=None,mode=None)
#os.mkdir("D:\\deam")        #创建目录，如果目录存在，会抛出异常

'''
if not os.path.exists("D:\\deam"):
    os.mkdir("D:\\deam")
else:
    print("该目录已经存在！！！！")
'''


#创建一个递归函数，用于创建目录

def mkdir(path):    #创建一个递归函数用于创建目录
    if not os.path.isdir(path):  #判断是否为路径
        mkdir(os.path.split(path)[0])
    else:
        return
    os.mkdir(path)      #创建目录

mkdir('D:\\deam\\test\\aaa')


#创建多级目录的函数
#os.makedirs()
"""makedirs(name [, mode=0o777][, exist_ok=False])"""
os.makedirs("D:\\deam\\test\\bbb")