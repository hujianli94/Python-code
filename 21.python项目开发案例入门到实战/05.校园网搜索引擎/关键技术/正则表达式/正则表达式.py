#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/12 16:49
# filename: 正则表达式.py
import re
'''
test = "用户输入的字符串"
if re.match(r'正则表达式', test):
    print("ok")
else:
    print('failed')
'''

# 返回一个Match对象
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))  # <_sre.SRE_Match object; span=(0, 9), match='010-12345'>

print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))  # '010 12345'不匹配规则，返回None


