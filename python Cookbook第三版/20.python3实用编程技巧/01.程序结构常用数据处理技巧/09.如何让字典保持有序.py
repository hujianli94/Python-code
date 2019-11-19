#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 11:39
# filename: 09.如何让字典保持有序.py

from collections import OrderedDict
from itertools import islice

d = OrderedDict()
d['e'] = 5
d['d'] = 4
d['c'] = 3
d['b'] = 2
d['a'] = 1

print(d)  # OrderedDict([('e', 5), ('d', 4), ('c', 3), ('b', 2), ('a', 1)])


# OrderedDict字典，在迭代操作时，它会保持元素被插入时的顺序

def query_by_order(d, a, b=None):
    if b is None:
        b = a + 1
    return list(islice(d, a, b))


# 第五个key
res1 = query_by_order(d, 4)
print(res1)  # ['a']

# 第二个和第三个key
res2 = query_by_order(d, 1, 3)
print(res2)  # ['d', 'c']
