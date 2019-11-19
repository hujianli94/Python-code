#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/9 15:43
# filename: 单例模式2.py

'''
1.只允许singleton类生成一个实例
2.已经有一个实例，重复提供同一个对象
'''


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print("Object created", s)
print(id(s))

s1 = Singleton()
print("Object created", s1)
print(id(s1))
