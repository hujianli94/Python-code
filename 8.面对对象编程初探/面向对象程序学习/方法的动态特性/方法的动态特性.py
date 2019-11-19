#!/usr/bin/env python
#-*- coding:utf8 -*-
class Fruit(object):
    pass

def add(self):          #定义在类外的函数
    print("grow...")

if __name__ == '__main__':
    Fruit.grow = add            #将函数加到方法中
    fuit = Fruit()              #实例化类
    fuit.grow()                 #调用类中的方法
