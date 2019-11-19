#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
import sys  #加载sys模块
if len(sys.argv) != 2:      #判断输入参数是否为2
    print("Please supply a filename")
    raise SystemExit(1)

f = open(sys.argv[1])       #命令行上参数1的文件名
lines = f.readlines()                   #将所有行读到一个列表中
f.close()

#将所有输入值从字符串转换为浮点数
fvalues = [float(line) for line in lines]

#打印最小值和最大值
print("The minimum value is  ",min(fvalues))
print("The maximum value is  ",max(fvalues))
'''

fruit1 = ['apple','orange']
fruit2 = ['pear','grape']
fruit1.extend(fruit2)
print(fruit1)
for i,v in enumerate(fruit1):
    print(i, v)
