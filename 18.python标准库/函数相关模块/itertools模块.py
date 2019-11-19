#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/17 14:00
# filename: itertools模块.py
import itertools

print([e for e in dir(itertools) if not e.startswith("_")])

import itertools as it

# 使用count(10,3)生成13、16、19....的迭代器
for e in it.count(10, 3):
    print(e)
    if e > 20:
        break
    print("---------------------")

my_counter = 0
# cycle用于对序列生成无限循环的迭代器
for e in it.cycle(["python", "kotlin", "Swift"]):
    print(e)
    # 用于跳出无限循环
    my_counter += 1
    if my_counter > 7:
        break
print("--------------------------")

# repeat用于生成n个元素重复的迭代器
for e in it.repeat("python", 3):
    print(e)
