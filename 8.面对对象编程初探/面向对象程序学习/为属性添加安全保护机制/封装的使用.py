#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/16 19:13
# filename: 封装的使用.py
class Plan:
    p_Count = 0

    def __init__(self, __name, __category, __carry):
        # 隐藏属性
        self.__name = __name
        self.__category = __category
        self.__carry = __carry

    def setCarry(self, __carry):
        if __carry > 0:
            self.__carry = __carry
        else:
            print("载客量的数值不对", __carry)

    def getCarry(self):
        return self.__carry


p1 = Plan("平安", "波音777", 380)
p1.setCarry(-40)
carryNum = p1.getCarry()
print("飞机的载客量是:{}".format(carryNum))
p1.setCarry(240)
carryNum = p1.getCarry()
print("飞机的载客量是:{}".format(carryNum))

'''
载客量的数值不对 -40
飞机的载客量是:380
飞机的载客量是:240
'''