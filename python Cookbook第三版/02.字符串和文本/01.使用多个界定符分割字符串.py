#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/29 15:06
# filename: 01.使用多个界定符分割字符串.py

line = 'asds asdsad; dsadasd,dasd,dasdasd,hujijjj'

import re

print(re.split(r'[;,\s]\s*', line))

fields = re.split(r'(;|,|\s)\s*',line)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
