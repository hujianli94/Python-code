#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 19:23
# filename: 08.查找两个字典的相同点.py
a = {
    "x": 1,
    "y": 2,
    "z": 3
}

b = {
    "w": 10,
    "x": 11,
    "y": 2

}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())


# 字典构造一个排除几个指定键的新字典
c = {key: a[key] for key in a.keys() - {"z", "w"}}
print(c)
