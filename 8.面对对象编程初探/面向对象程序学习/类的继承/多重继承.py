#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
经典类:深度优先
新式类:广度优先
"""


class PrntA:
    namea = 'PrntA'

    def set_value(self, a):
        self.a = a

    def set_name(self, namea):
        PrntA.namea = namea

    def info(self):
        print("PrntA：{}，{}".format(PrntA.namea, self.a))


class PrntB:
    nameb = "PrntB"

    def set_nameb(self, nameb):
        PrntB.nameb = nameb

    def info(self):
        print("PrntB:{}".format(PrntB.nameb))


class Sub(PrntA, PrntB):
    pass


class Sub2(PrntB, PrntA):
    pass


class Sub3(PrntA, PrntB):
    def info(self):
        PrntA.info(self)
        PrntB.info(self)


print()
print("使用第一个子类：")
sub = Sub()
sub.set_value("aaaaa")
sub.info()
sub.set_nameb("BBBB")
sub.info()

print()
print("使用第二个子类：")
sub2 = Sub2()  # 实例化类Sub2
sub2.set_value("aaaa")
sub2.info()
sub2.set_nameb("BBBBB")
sub2.info()

print()
print("使用第三个子类：")
sub3 = Sub3()  # 实例化类Sub2
sub3.set_value("aaaa")
sub.info()
sub3.set_nameb("BBBB")
sub.info()
