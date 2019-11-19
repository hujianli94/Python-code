#!/usr/bin/env python
#-*- coding:utf8 -*-
class Student:
    __slots__ = ["name","age","sex","number"]
    def __init__(self,name,age,sex,number):
        self.name = name
        self.age = age
        self.sex = sex
        self.number = number

hu = Student("hu","18","man","19")
print(dir(hu))
