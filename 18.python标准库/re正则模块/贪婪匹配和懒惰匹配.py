#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/21 17:31
# filename: 贪婪匹配和懒惰匹配.py
import re

# 使用贪婪匹配
m = re.search(r'\d{5,8}', '87654321')
print(m)            #<_sre.SRE_Match object; span=(0, 8), match='87654321'>
print(m.group())    #87654321

# 使用惰性匹配
m = re.search(r'\d{5,8}?', '87654321')      #<_sre.SRE_Match object; span=(0, 5), match='87654'>
print(m)
print(m.group())                            #87654
