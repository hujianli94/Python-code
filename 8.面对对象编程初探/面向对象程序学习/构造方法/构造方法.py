#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/18 0:02
# filename: 构造方法.py
class Animal(object):
    """
    定义动物类
    """

    def __init__(self, age, sex=1, weight=0.0):
        # 定义实例变量，实例化时自动载入
        self.age = age
        self.sex = sex
        self.weight = weight


a1 = Animal(2, 0, 10.0)
a2 = Animal(1, weight=5.0)
a3 = Animal(1, sex=0)

print("a1年龄：{0}".format(a1.age))
print("a2体重：{0}".format(a2.weight))
print("a3性别：{0}".format("雌雄" if a3.sex == 0 else "雄性"))
