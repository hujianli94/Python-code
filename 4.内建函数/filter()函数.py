#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 23:42
# filename: filter()函数.py

users = ["Tony", "Tom", "Ben", "Alex"]
users_list = filter(lambda x: str(x).startswith("T"), users)
print(list(users_list))

number_list = range(1, 11)
number_filter = filter(lambda it: it % 2 == 0,number_list)
print(list(number_filter))
