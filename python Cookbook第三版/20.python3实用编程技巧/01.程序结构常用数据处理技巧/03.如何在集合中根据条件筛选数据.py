#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 11:20
# filename: 03.如何在集合中根据条件筛选数据.py
from random import randint

s = {randint(0, 20) for _ in range(20)}
print(s)

hu1 = {x for x in s if x % 3 == 0}
print(hu1)
