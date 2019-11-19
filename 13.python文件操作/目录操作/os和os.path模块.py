#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
os模块是python 内置与操作系统功能和文件系统相关的模块，
该模块中的语句的执行结果通常与操作系统有关
os.path模块
'''
import os
print(os.name)      #获取操作系统信息
print(os.linesep)      #获取操作系统操作符
print(os.path.abspath("D:\GitHub\\21天python\python IO"))
print(os.path.join(r'D:\GitHub',r'demo\test.txt'))