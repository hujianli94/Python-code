#!/usr/bin/env python
#-*- coding:utf8 -*-

class Geese:
    '''
    大雁类
    '''
    neck = '脖子较长'   #类属性
    wing = '翅膀频率高'
    leg = '腿位于身体的中心支点，行走自如'
    number = 0

    def __init__(self):  #定义构造方法
        Geese.number +=1
        print('\n我是第{}只大雁类，我有以下特征：'.format(Geese.number))
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)

    def fly(self, state):        #飞行方法
        print(state)



list1 = []
for i in range(4):
    list1.append(Geese())

print("一共有{}只大雁!".format(Geese.number)) #输出大雁的只数
Geese.beak = "这是添加的一个属性,属性名称beak."
print(list1[1].beak)