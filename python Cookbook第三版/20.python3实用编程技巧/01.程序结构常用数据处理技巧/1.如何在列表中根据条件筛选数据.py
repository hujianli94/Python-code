#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 22:34
# filename: 1.如何在列表中根据条件筛选数据.py

data = [-1, 2, 3, -4, 5]

# 方式1
new_data = []
for i in data:
    if i > 0:
        new_data.append(i)
print(new_data)

# 方式2，列表推导式
new_data2 = [i for i in data if i > 0]
print(new_data2)

# 方式3，filter函数
new_data3 = list(filter(lambda i: i > 0, data))
print(new_data3)
