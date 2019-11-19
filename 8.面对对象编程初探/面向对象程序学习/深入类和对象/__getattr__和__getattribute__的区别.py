#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
object.__getattr__(self, name)
找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常。

object.__getattribute__(self, name)
无条件被调用，通过实例访问属性。如果class中定义了__getattr__()，则__getattr__()不会被调用（除非显示调用或引发AttributeError异常）
'''

class User:
    def __init__(self, info={}):
        self.info = info

    #__getattr__是在查找不到属性的时候调用
    def __getattr__(self, item):
        return self.info[item]

    #__getattribute不管属性存不存在，都访问这个
    def __getattribute__(self, item):
        return "zhang_derek"


if __name__ == '__main__':
    user = User(info={"name":"derek","age":24})
    #不管属性存不存在，都走__getattribute__
    print(user.name)    #zhang_derek     #即使属性存在也走__getattribute__
    print(user.test)     #zhang_derek    #不存在的属性也能打印
    print(user.company)   #zhang_derek   #不存在的属性也能打印