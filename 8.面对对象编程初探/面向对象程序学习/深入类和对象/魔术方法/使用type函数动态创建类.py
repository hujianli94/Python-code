#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/14 13:09
# filename: 使用type函数动态创建类.py
def fn(self):
    print("fn函数")


# 使用type()定义Dog类
Dog = type("Dog", (object,), dict(walk=fn, age=6))

"""
参数1：创建的类名
参数2：继承的父类集合，必须要有一个逗号
参数3：字典对象，key为变量名或者方法名，value如果是函数代表方法，如果是普通值，代表类变量
"""

#創建Dog对象
d = Dog()

#分别查看d、Dog的类型
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)

