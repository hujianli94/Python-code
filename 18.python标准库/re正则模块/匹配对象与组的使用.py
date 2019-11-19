#!/usr/bin/env python
# -*- coding:utf8 -*-

import re  # 导入re模块

s = """
life can be dreams,
Life can be great thoughts;
Life can mean a person,
Sitting in a court.
"""
# 编译正则表达式，匹配所有包含字母“a”的单词
r = re.compile('\\b(?P<first>\w+)a(\w+)\\b')
m = r.search(s)
print(m.groupdict())  # {'first': 'c'}
print(m.groups())  # ('c', 'n')
# 从指定位置开始重新搜索
m = r.search(s, 9)
print(m.group())  # dreams
print(m.group((1)))  # dre
print(m.group((2)))  # ms
print(m.group(1, 2))  # ('dre', 'ms')
print(m.groupdict())  # {'first': 'dre'}
print(m.groups())  # ('dre', 'ms')
