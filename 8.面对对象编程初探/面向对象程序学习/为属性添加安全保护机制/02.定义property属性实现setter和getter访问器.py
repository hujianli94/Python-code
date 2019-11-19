#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/23 10:18
# filename: 01.定义property属性.py

class Animal(object):
    """
    定义动物类
    """

    def __init__(self, age, sex=1, wight=0.0):
        self.age = age
        self.sex = sex
        self.__wight = wight

    @property
    def weight(self):  # 代替get_wight(self):
        return self.__wight

    @weight.setter
    def wight(self, wight):  # 代替set_weight(self,wight):
        self.__wight = wight


if __name__ == '__main__':
    a1 = Animal(18, 0, 10.0)
    print("a1的体重：{0:0.2f}".format(a1.wight))
    a1.wight = 123.45
    print("a1的体重：{0:0.2f}".format(a1.wight))
