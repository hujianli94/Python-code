#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
语法：

isinstance(object, classinfo)
object 是变量，classinfo 是类型即 (tuple,dict,int,float,list,bool等) 和 class类
'''
print(isinstance(1,int))
print(isinstance(1.0,float))
print(isinstance("aa",str))
print(isinstance(1,list))


print()
print()
'''
type()与isinstance()的区别：

共同点：两者都可以判断对象类型
不同点：对于一个 class 类的子类对象类型判断，type就不行了，而 isinstance 可以。
'''

class A(object):
    pass

class B(A):
    pass


b = B()
print(isinstance(b,B))
print(isinstance(b,A))
print(" type ".center(100,"*"))
print(type(b) is B)           #True
#b指向了B()对象，虽然A是B的父类，但是A是另外一个对象，它们的id是不相等的
print(type(b) is A)           #False