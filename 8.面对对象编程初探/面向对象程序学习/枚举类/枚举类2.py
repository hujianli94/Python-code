#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/31 18:26
# filename: 枚举类2.py

import enum


class ORientation(enum.Enum):
    # 为序列值指定value值
    EAST = "东"
    SOUTH = "南"
    WEST = "西"
    NORTH = "北"

    def info(self):
        print("这是一个代表【{0}】方向的枚举".format(self.value))


print(ORientation.SOUTH)
print(ORientation.SOUTH.value)
# 通过枚举变量访问枚举
print(ORientation['WEST'])
# 通过枚举值来访问枚举
print(ORientation('南'))

# 通过枚举的info()方法
ORientation.EAST.info()

# 遍历枚举的所有成员
for name, number in ORientation.__members__.items():
    print(name, "===>", number, ",", number.value)
