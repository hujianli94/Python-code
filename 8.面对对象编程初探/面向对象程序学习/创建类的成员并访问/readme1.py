#!/usr/bin/env python
#-*- coding:utf8 -*-
class Geese:
    '''
    大雁类
    '''
    neck = '脖子较长'   #类属性
    wing = '翅膀频率高'
    leg = '腿位于身体的中心支点，行走自如'

    def __init__(self):  #定义构造方法
        print('我是大雁类，我有以下特征：')
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)

    def fly(self, state):        #飞行方法
        print(state)

beak_1 = "喙的基部较高，长度和头的长度几乎相等"
wing_1 = "翅膀长而尖"
claw_1 = "爪子是噗状的"
# windGoose = Geese(beak_1, wing_1, claw_1)
# print()
# windGoose.fly("我飞行的时候，一会排成人字，一会排成一字")
print()
print("我的形态特征是：")
windGoose = Geese()
