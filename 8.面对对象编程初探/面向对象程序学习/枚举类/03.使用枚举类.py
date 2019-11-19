#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/23 12:35
# filename: 03.使用枚举类.py

import enum


# 防止常量成员值重复，使用@enum.unique装饰器
@enum.unique
class WeekDays(enum.IntEnum):
    # 限制常量只能为整数使用 enum.IntEnum
    # 枚举常量列表
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 10


day = WeekDays.THURSDAY

if day.value > 5:
    print("学习、娱乐....")
else:
    print("工作......")

"""
工作......
"""