#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/16 19:06
# filename: 实例属性操作方法.py
class Plan:
    """
    This is Plan
    """
    p_Count = 0

    def __init__(self, name, creategory):
        self.name = name
        self.creategory = creategory
        self.p_Count += 1


p1 = Plan("hujianli", "boy722")
print(getattr(p1, "name"))
setattr(p1, "name", "huxiaojian")
print(getattr(p1, "name"))
print(hasattr(p1, 'name'))
print(hasattr(p1, 'name1'))
delattr(p1, "name")
print(getattr(p1, "name"))      # 报错，属性不存在
