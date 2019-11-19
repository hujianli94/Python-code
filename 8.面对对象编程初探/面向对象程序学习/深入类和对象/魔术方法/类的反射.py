#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
hasattr:判断一个对象是否有对应字符串方法
getattr:获取方法
setattr:添加方法
delattr:删除方法
"""

def bulk(self):
    '''
    添加的方法
    :return:
    '''
    print("%s is yelling ...." % self.name)


class Dog(object):
    def __init__(self, name):
        self.name = name


    def eat(self, food):
        print("{} is eating.....".format(self.name, food))

    def call(self,call):
        print("{} is wang wang wang ...".format(self.call))

d = Dog("jianli")
choice = str(input(">>:")).strip()

if hasattr(d, choice):       #输入字符串，判断是否有对应的字符串的方法
    func1 = getattr(d, choice)      #获取方法
    func1('')
else:
    setattr(d, choice, bulk) #d.talk = bulk   #通过setattr在类外部添加方法
    func2 = getattr(d, choice)
    func2(d)

print(d.__dict__)

setattr(d,choice,18)
print(d.__dict__)

print("调用delattr删除类中的属性".center(100,"*"))
delattr(d,choice)
print(d.__dict__)


