#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/17 14:15
# filename: 函数1.py
from functools import *

# print([x for x in dir(functools) if not x.startswith("_")])

print(reduce(lambda x, y: x + y, range(5)))
print(reduce(lambda x, y: x + y, range(6)))

# 设置初始值为10
print(reduce(lambda x, y: x + y, range(6), 10))
print("------------------------------------------")


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "User[name={}]".format(self.name)


def old_cmp(ul, u2):
    '''
    定义一个老式的比较函数，User的name越长，User越大
    :param ul:
    :param u2:
    :return:
    '''
    return len(ul.name) - len(u2.name)


my_date = [User('Kotlin'), User('Swift'), User('Go'), User('Java')]

my_date.sort(key=cmp_to_key(old_cmp))
print(my_date)
print("------------------------------")
