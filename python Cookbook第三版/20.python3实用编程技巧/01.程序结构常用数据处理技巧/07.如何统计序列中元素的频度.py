#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 11:37
# filename: 07.如何统计序列中元素的频度.py

# 1.6如何统计序列中元素的频度
from random import randint
from collections import Counter

data = [randint(1, 5) for _ in range(1, 20)]
print(data)  # [5, 2, 1, 2, 5, 3, 1, 1, 1, 4, 2, 5, 3, 2, 3, 5, 1, 2, 5]

# 计算频度最高的是三个数
c = Counter(data)
print(c.most_common(3))  # [(1, 5), (3, 4), (2, 4)]
