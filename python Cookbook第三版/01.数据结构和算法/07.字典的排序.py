#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 19:15
# filename: 07.字典的排序.py
from collections import OrderedDict

d = OrderedDict()

d["hujianli1"] = 1
d["hujianli2"] = 2
d["hujianli3"] = 3
d["hujianli4"] = 4

print(d)
for key in d:
    print(key, d[key])


# 控制json编码后的字段的顺序。
import json
print(json.dumps(d))
print(type(json.dumps(d)))