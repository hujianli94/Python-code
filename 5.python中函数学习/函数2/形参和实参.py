#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
值传递 ----> 不可变对象
引用传递 ----->  可变对象

'''

def deam(obj):
    print("原值:", obj)
    obj +=obj

#调用函数，值传递
print("="*10,"值传递","="*10)
mot = "唯有在追赶的时候，你才能真正的奔跑"       #不可变对象
print("函数调用前：",mot)
deam(mot)
print("函数调用后：",mot)


print("="*10,"引用传递","="*10)
list = [1,2,3,4,5,6]                            #可变对象
print("函数调用前：",list)
deam(list)
print("函数调用后：",list)
