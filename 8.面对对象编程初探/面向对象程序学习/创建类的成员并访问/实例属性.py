#!/usr/bin/env python
#-*- coding:utf8 -*-
class Geese:
    '''
    大雁类
    '''
    def __init__(self):
        self.neck = '脖子较长'
        self.wing = '翅膀振翅频率高'
        self.leg = '腿位于身体的中心支点，行走自如'
        print("我属于雁类，我有以下特征:")
        print(self.neck)
        print(self.wing)
        print(self.leg)

geese = Geese()         #实例化类对象
geese1 = Geese()
geese1.leg = "通过腿我可以行走"
print("geese:",geese.leg)        #显示一条关于geese的信息
print()
print("geese1:",geese1.leg)        #显示一条关于geese1的信息