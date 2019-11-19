#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/9 15:39
# filename: 单例模式1.py

class Person:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print("-----------------> init")


hu1 = Person()
hu2 = Person()
hu3 = Person()

print(id(hu1))
print(id(hu2))
print(id(hu3))
