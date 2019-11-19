#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/23 21:57
# filename: 装饰类002.py

def addSex(myClass):
    class InnerClass:
        def __init__(self, name, age, sex):
            self.sex = sex
            self.wrapper = myClass(name, age)

        def showInfo(self):
            self.wrapper.showInfo()
            print("sex:{}".format(self.sex))

    return InnerClass


@addSex
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print("name:{}".format(self.name))
        print("age:{}".format(self.age))


if __name__ == '__main__':
    p = Person("Tom", 18, "MALE")
    p.showInfo()

"""
name:Tom
age:18
sex:MALE
"""