#!/usr/bin/env python
#-*- coding:utf8 -*-

class Foo:
    name = "class_name"

    def __init__(self,name):
        self.name = name

    def ord_fun(self):
        """ 定义普通方法，至少有一个self参数"""
        print("普通方法")

    @classmethod
    def class_func(cls):
        ''' 定义类方法，至少有一个cls参数 '''
        print("类方法", cls.name)

    @staticmethod
    def static_func():
        ''' 定义静态方法，无默认参数'''
        print("静态方法")


# 调用普通方法
f = Foo("hujianli")
f.ord_fun()


# 调用类方法
Foo.class_func()

#调用静态方法
Foo.static_func()










