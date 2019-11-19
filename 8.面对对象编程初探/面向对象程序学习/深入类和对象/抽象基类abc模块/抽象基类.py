#!/usr/bin/env python
#-*- coding:utf8 -*-
#判断类是否有某种属性


#抽象基类的作用类似于JAVA中的接口。在接口中定义各种方法，然后继承接口的各种类进行具体方法的实现。
# 抽象基类就是定义各种方法而不做具体实现的类，任何继承自抽象基类的类必须实现这些方法，否则无法实例化
#抽象基类（abc模块）

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(["11", "22", "33"])

#hasattr判断类有没有某种属性，方法也是类的属性
print(hasattr(com,"__len__"))   #True

#虽然用hasattr可以判断，但正确的方式是定义一个抽象基类

#我们在某些情况下希望判定某个对象的类型，可以用抽象基类
from collections.abc import Sized
print(isinstance(com,Sized))    #True
print(len(com))
