#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/9 15:45
# filename: 单例模式中懒汉式实例.py

class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called ..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()#实例化Singleton类
print("Object created",Singleton.getInstance())

s1 = Singleton()  #再次实例类的时候会走else分支

