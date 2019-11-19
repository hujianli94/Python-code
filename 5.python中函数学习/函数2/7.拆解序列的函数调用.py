#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
拆解元祖    提供位置参数
拆解字典    提供关键字参数
'''

def mysum(a,b):
    return a+b

print("拆解元祖调用：")
print(mysum(*(3, 4)))        #调用时拆解元祖作为位置参数
print("拆解字典调用：")
print(mysum(**{'a':3,'b':4}))   #调用时拆解字典作为关键字参数
