#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/23 10:18
# filename: 01.定义属性.py

class Animal(object):
    """
    定义动物类
    """

    def __init__(self, age, sex=1, wight=0.0):
        self.age = age
        self.sex = sex
        self.__wight = wight

    def set_weight(self, wight):            # serrer访问器
        self.__wight = wight

    def get_wight(self):                    # getter访问器
        return self.__wight


if __name__ == '__main__':
    a1 = Animal(18, 0, 10.0)
    print("a1的体重：{0:0.2f}".format(a1.get_wight()))
    a1.set_weight(20.0)
    print("a1的体重：{0:0.2f}".format(a1.get_wight()))

