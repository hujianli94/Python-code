#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/9 15:48
# filename: 装饰器实现单例.py

class cls_decorator:
    def __init__(self, f):
        self.f = f
        self.__intance = {}

    def __call__(self, *args, **kwargs):
        if self.f not in self.__intance:
            self.__intance[self.f] = self.f()
        return self.__intance[self.f]


@cls_decorator
class Singleton:
    def __init__(self):
        print("---------->Singleton init ")


print(Singleton)
hu1 = Singleton()
hu2 = Singleton()
print(hu1 is hu2)
print(id(hu1))
print(id(hu2))
