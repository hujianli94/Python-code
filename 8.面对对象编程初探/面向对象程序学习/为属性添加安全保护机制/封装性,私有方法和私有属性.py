# !/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/18 7:38
# filename: 封装性,私有方法和私有属性.py
class Animal(object):
    def __init__(self, age, sex=1, weight=0.0):
        self.age = age
        self.sex = sex
        self.__weight = weight

    def eat(self):
        self.__weight += 0.5
        self.__run()
        print("eat.....")

    def __run(self):
        """
        私有方法
        :return:
        """
        self.__weight -= 0.01
        print("run.....")


a1 = Animal(18, 0, 10.0)
# print(dir(a1))
a1.eat()
# a1.run()            #会报错，私有方法不能直接调用
# a1._Animal__run()
print(a1._Animal__weight)
