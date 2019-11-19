#!/usr/bin/env python
#-*- coding:utf8 -*-
class Descriptor(object):
    def __get__(self, instance, owner):
        print("in __get__",instance,owner)
        return instance
    def __set__(self, instance, value):
        print("in __set__")

    def __delete__(self, instance):
        print("in __del__")


class A(object):
    x = Descriptor()


a = A()
a.x = 5
print(a.x)