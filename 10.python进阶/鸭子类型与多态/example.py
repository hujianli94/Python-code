#!/usr/bin/env python
#-*- coding:utf8 -*-
#关注不是对象的类型本身，而是它是如何使用的

class Duck:
    def __init__(self,name="duck"):
        self.name = name

    def quck(self):
        print("嘎嘎嘎")

class Cat:
    def __init__(self,name='cat'):
        self.name = name

    def quck(self):
        print("喵喵喵")

class Tree:
    def __init__(self,name="Tree"):
        self.name = name

def duck_demo(object):
    object.quck()

if __name__ == '__main__':
    duck = Duck()
    cat = Cat()
    tree = Tree()
    duck_demo(duck)
    duck_demo(cat)
