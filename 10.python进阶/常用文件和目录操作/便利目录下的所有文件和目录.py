#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
os.walk()函数返回的是一个可以迭代的生成器，要处理遍历得到的结果，可以使用for语句来循环处理
os.walk(path)
第一项为遍历的目录名（字符串）
第二项为遍历目录中的子目录列表
第三项为遍历目录中所有文件的列表
'''
import os
print(os.linesep)   #平台下的行分割符
print(os.pathsep)   #目录名分隔符
for i in os.walk('.\\'):
    print(i)
