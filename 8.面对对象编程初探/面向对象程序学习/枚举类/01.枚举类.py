#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/18 8:19
# filename: 01.枚举类.py
"""
枚举是用来管理一组相关的有限个数常量的集合，使用枚举可以提高程序的可读性，使代码更清晰且更易于维护。
python提供枚举类型，本质上是一种类
"""
"""
python中定义枚举类的语法如下：

class 枚举名(enum.Enum):
    枚举常量列表
"""
'''
限制常量只能为整数使用 enum.IntEnum

防止常量成员值重复，使用@enum.unique装饰器
'''

import enum


class WeekDays(enum.Enum):
    # 枚举常量列表
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 10



day = WeekDays.FRIDAY
print(day)
print(day.name)
print(day.value)
print(day.THURSDAY.name)
print(day.THURSDAY.value)


"""
WeekDays.FRIDAY
FRIDAY
10
THURSDAY
4
"""