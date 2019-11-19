#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/16 19:21
# filename: 类继承代码.py
class Plan:
    """
    飞机类
    """
    pCount = 0

    def __init__(self, __name, __category):
        self.__name = __name
        self.__category = __category
        Plan.pCount += 1

    def showPlanInfo(self):
        print("飞机的名称：{}，类型：{}".format(self.__name, self.__category))


class AvionPlan(Plan):
    """
    军用飞机
    """

    def __init__(self, __name, __category, __gun):  # 子类构造方法
        super(AvionPlan, self).__init__(__name, __category)  # 调用父类构造方法
        self.__gun = __gun  # 子类特有属性

    def setGun(self, __gun):
        if __gun > 0:
            self.__gun = __gun
        else:
            print("携带的枪炮数值不对", __gun)

    def getGun(self):
        return self.__gun

    def showAvionPlan(self):
        print("携带的枪炮数量：{}".format(self.__gun))


class CivilPlan(Plan):
    """
    民用载客飞机
    """

    def __init__(self, __name, __category, __carry):  # 子类构造方法
        super(CivilPlan, self).__init__(__name, __category)  # 调用父类构造方法
        self.__carry = __carry  # 子类特有属性

    def setCarry(self, __carry):
        if __carry > 0:
            self.__carry = __carry
        else:
            print("载客量不对", __carry)

    def getCarry(self):
        return self.__carry

    def showCivilPlan(self):
        print("载客数量：{}".format(self.__carry))


if __name__ == '__main__':
    p1 = AvionPlan("凯旋", "歼10", 6)
    p1.showPlanInfo()
    p1.showAvionPlan()
    print("-" * 100)
    p2 = CivilPlan("平安", "波音", 320)
    p2.showPlanInfo()
    p2.showCivilPlan()
    print(Plan.pCount)
    print(p1.pCount)
    print(p2.pCount)

    p3 = AvionPlan("凯旋2", "歼12", 10)
    p3.showPlanInfo()
    p3.showAvionPlan()
    print(Plan.pCount)
    print(p1.pCount)
    print(p2.pCount)
'''

飞机的名称：凯旋，类型：歼10
携带的枪炮数量：6
----------------------------------------------------------------------------------------------------
飞机的名称：平安，类型：波音
载客数量：320
2
2
2
飞机的名称：凯旋2，类型：歼12
携带的枪炮数量：10
3
3
3

'''
