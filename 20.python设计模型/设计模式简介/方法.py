#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
他们表示对象的行为
方法可以对属性进行处理，从而实现所需的功能
'''

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_person(self):
        return "<Person (%s,%s)>" %(self.name,self.age)

hu = Person("hujianli","22")
print("Type of Object: ",type(hu),"Memory Address:",id(hu))