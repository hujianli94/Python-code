#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/30 9:41
# filename: 05.删除字符串中不需要的字符.py
s = ' hello world \n'

print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '-----hello====='
print(t.strip('-'))
print(t.strip('='))
print(t.strip('-='))

s = ' hello     world \n'
print(s.strip())

print(s.replace(' ', '').strip())

import re

print(re.sub('\s+', ' ', s))


with open("04.多行匹配模式.py", encoding="utf-8") as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
