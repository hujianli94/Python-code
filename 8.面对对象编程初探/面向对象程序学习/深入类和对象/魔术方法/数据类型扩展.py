#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/15 14:27
# filename: 数据类型扩展.py
# 定义ValueDict类，继承dict类
class ValueDict(dict):
    # 定义构造函数
    def __init__(self, *args, **kwargs):
        # 调用父类的构造函数
        super(ValueDict, self).__init__(*args, **kwargs)

    # 新增一个方法
    def getkeys(self, val):
        result = []
        for key, value in self.items():
            if value == val:
                result.append(key)
        return result


my_dict = ValueDict(语文=90, 数学=70, 英语=90)
print(my_dict.getkeys(90))
my_dict["编程"] = 90
print(my_dict.getkeys(90))
