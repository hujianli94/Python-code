#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
类的公有属性
属于这个类的所有对象，都可以访问的属性，叫做公有属性
"""
#成员属性
class Person(object):
    '''
    成员属性
    '''
    def __init__(self,name,job,phone,address):
        self.name = name
        self.job = job
        self.phone = phone
        self.__address = address

    def get_private(self):
        return self.__address

    def sayhai(self):
        print("Hello {}".format(self.name))

p1 = Person("bigberg","Doctor","123","hz")
p2 = Person("hujianli","IT","123","hjl")
print(p1.job,p2.job)


class Person(object):
    '''
    公有属性
    '''
    nationality = 'CN'   #定义公有属性
    def __init__(self,name,job,phone,address):
        self.name = name
        self.job = job
        self.phone = phone
        self.address = address

    def sayhi(self):
        print("hello {}".format(self.name))

p1 = Person("Big","Doctor",'123','hjl')
p2 = Person("smiler","IT",'456','hxj')
print(p1.nationality)
print(p2.nationality)
p1.nationality = "change_hu"
print(p1.nationality)
print(p2.nationality)
#公有属性而言，所有实例对象访问它得到的值是一样的
#p1修改了公有属性的值，不会影响到p2


