#!/usr/bin/env python
#-*- coding:utf8 -*-

def change(aint,alst):
    aint = 0                    #aint的值
    alst[0] = 0             #修改alst第一个值为0
    alst.append(4)          #在alst中添加一个元素4
    print("函数中aint:",aint)  #输出函数中aint的值
    print("函数中alst:",alst)  #输出函数中的alst的值

aint = 3
alst = [1,2,3]
print("调用前aint:",aint)
print("调用前alst:",alst)
change(aint,alst)
print("调用后aint:",aint)
print("调用后alst:",alst)