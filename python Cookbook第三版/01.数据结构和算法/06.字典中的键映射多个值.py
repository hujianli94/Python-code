#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 16:47
# filename: 06.字典中的键映射多个值.py
"""
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['c'].append(4)
print(d)

s = defaultdict(set)
s['a'].add(1)
s['a'].add(2)
s['c'].add(4)
print(s)

"""

d = {}
d.setdefault('hu', []).append(1)
d.setdefault('hu', []).append(2)
d.setdefault('hu', []).append(4)
print(d)