#!/usr/bin/env python
# -*- coding:utf8 -*-
import re

'''
re.split(pattern,string[,maxsplit=0],[flags])
#pattern    正则表达式模式；
#string     要分割的字符串
maxsplit    可选参数，最大分割次数
flags       re.I 不区分大小写     re.A 让\w不匹配汉字
'''
s = "Life can be bad"

print(re.split(' ', s))  # ['Life', 'can', 'be', 'bad']
# 只分割一次
r = re.split(' ', s, 1)  # ['Life', 'can be bad']
print(r)  # Life
for i in r:
    print(i)  # can be bad

# 使用字母"b"分割字符
print(re.split('b', s))  # ['Life can ', 'e ', 'ad']

print()
str = 'a b    c'
print(re.split(r'\s+', str))            #['a', 'b', 'c']

str2 = 'a,b, c    d'
print(re.split(r'[\s\,]+', str2))       #['a', 'b', 'c', 'd']

str3 = 'a,b;; c  d'
print(re.split(r'[\s\,\;]+', str3))     #['a', 'b', 'c', 'd']

