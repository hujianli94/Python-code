#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/31 18:44
# filename: 枚举类3.py

import enum


class Man(enum.Enum):
    MALE = "男", "帅气"
    FEMALE = "女", "美丽"

    def __init__(self, cn_name, desc):
        self._cn_name = cn_name
        self._desc = desc

    @property
    def desc(self):
        return self._desc

    @property
    def cn_name(self):
        return self._cn_name


#访问MALE的name
print("MALE的name:{}".format(Man.MALE.name))
#访问MALE的value
print("MALE的value:{}".format(Man.MALE.value))


#访问MALE自定义的cn_name属性
print("访问MALE自定义的cn_name属性:{}".format(Man.MALE.cn_name))


#访问MALE自定义的desc属性
print("访问MALE自定义的desc属性:{}".format(Man.MALE.desc))


