#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 11:33
# filename: 06.如何根据字典中值的大小，对字典中的项进行排序.py

# 方式1

from random import randint

d = {k: randint(60, 100) for k in 'abcdefg'}
print(d)
# 第一种方法：使用列表解析或者zip()函数,把字典的keys和values反转过来
list1 = [(v, k) for k, v in d.items()]
# 或者使用zip()函数
# list2 = list(zip(d.values(),d.keys()))
print(list1)
list1 = sorted(list1, reverse=True)
print(list1)

# 方式2 使用sorted排序
p = sorted(d.items(), key=lambda item: item[1], reverse=True)
print(p)

# 对分数添加一个排名
d = {k: (i, v) for i, (k, v) in enumerate(p, 1)}
print(d)
