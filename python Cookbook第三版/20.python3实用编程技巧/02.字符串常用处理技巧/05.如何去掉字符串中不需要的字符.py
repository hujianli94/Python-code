#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 22:58
# filename: 05.05.如何去掉字符串中不需要的字符.py

s = "    hujianli     "
print(s.strip())  # hujianli

print(s.lstrip())  # hujianli

print(s.rstrip())  # hujianli

s1 = '-=+hujianli0001-=-+'
print(s1.strip())  # -=+hujianli0001-=-+
print(s1.strip('-='))  # +hujianli0001-=-+
print(s1.strip("-=+"))  # hujianli0001

# 删除固定位置，用切片，去掉下面的冒号
s2 = 'abc:123'
s2 = s2[:3] + s2[4:]
print(s2)  # abc123

# replace
s3 = '  abc  123  '
s3 = s3.strip()
s3 = s3.replace(' ', '')
print(s3)  # abc123

# 正则表达式re.sub()
s4 = '  \t  abc  \t  123  \n  '
import re

s4 = re.sub('[ \t\n]', '', s4)
print(s4)  # abc123
