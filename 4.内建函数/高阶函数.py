#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/10/29 17:28
# filename: 高阶函数.py
# dict1 = {"张申": 1220, "李四": 1200, "王五": 12289, "赵六": 262}
# result = sorted(dict1.items(), key=lambda x: x[1])
#
# from collections import OrderedDict
#
# d = OrderedDict()
# for i in result:
#     d[i[0]] = i[1]
# print(d)
#
# for k, v in d.items():
#     print(k, v)

# from functools import reduce
#
# reduce()


from functools import partial, wraps


def add(x, y):
    return x + y


# 给函数的参数绑定一个默认值
add1 = partial(add, 3)
x1 = add(3, 9)
print(x1)

x = add1(9)
print(x)

r = int("123", base=8)  # 83
print(r)
r = int('00101101', base=2)  # 45
print(r)

int2 = partial(int, base=2)
int2('100000')
print(int2)
