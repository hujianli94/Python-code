#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
可以使用__slots__限制实例的变量，比如，只允许Foo的实例添加name和age属性
"""


# def print_doc(self):
#     print("哈哈")
#
# class Foo:
#     __slots__ = ("name","age")
#     pass
#
# class AAA(object):
#     pass
#
# object1 = Foo()
# object2 = Foo()
#
# #动态添加实例变量
# object1.name = "hujianli"
# object2.age = 18
#
# # object.sex = "man"
#
# Foo.show = print_doc
# object1.show()
# object2.show()
#
# #因为内部有__slots__限制实例的变量
# print(Foo.__dict__)


class Dog:
    __slots__ = ["walk", "walk2", "age", "name"]

    def __init__(self, name):
        self.name = name


def hujianli(self):
    print("预先定义的hujianli方法")
    print("【{}】正在慢慢走向你".format(self.name))


d = Dog("Snoopy")

from types import MethodType

# 只允许为实例动态添加walk、age、name这三个属性或方法
d.walk = MethodType(hujianli, d)
d.walk2 = MethodType(lambda self, one_arg: print("这是lambda函数，Dog name is 【{}】 "
                                                 "传入参数：{}".format(self.name, one_arg)), d)
d.age = 5
d.walk()
d.walk2("参数测试1")
print()
print()
print("但不限制类来添加动态的属性，使用类来动态定义bar方法，正常输出")
# 但不限制类来添加动态的属性，使用类来动态定义bar方法，正常输出
Dog.bar = MethodType(hujianli, d)
Dog.bar()
# d.foo = 30      # 报错
