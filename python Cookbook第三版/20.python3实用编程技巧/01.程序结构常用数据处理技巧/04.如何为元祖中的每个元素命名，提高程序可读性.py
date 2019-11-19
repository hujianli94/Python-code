#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 11:23
# filename: 04.如何为元祖中的每个元素命名，提高程序可读性.py

def func(student):
    if student[1] < 18:
        pass

    if student[2] == 'male':
        pass


s1 = ('derek', 22, 'male', '111@qq.com')

# 第一种：使用枚举
from enum import IntEnum


class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3


print(s1[StudentEnum.NAME])
print(s1[StudentEnum.AGE])
print(s1[StudentEnum.SEX])
print(s1[StudentEnum.EMAIL])

print("*" * 50,"使用collections.namedtuple来实现", "*" * 50)
# 第二种：使用标准库中collections.namedtuple替代内置tuple
from collections import namedtuple

Student = namedtuple('student', ['name', 'age', 'sex', 'email'])
s2 = Student('derek', 22, 'male', '222@qq.com')
print(s2[0])  # derek
# 可以通过s2.name获取姓名
print(s2.name)  # derek
