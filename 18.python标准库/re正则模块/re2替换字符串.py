#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
re.sub(pattern,repl,string,count,[flags])    #替换在字符串中符合正则表达式的内容，返回替换后的字符串
pattern:模式字符串
repl：匹配后替换的字符串
string:需要匹配的对象
count：替换的次数
flags: re.I ,re.A

re.subn()   #返回一个元祖用来保存替换的结果和替换次数
'''

import re

s = "Life can be bad"
print(re.sub("bad", "good", s))  # Life can be good
print(re.sub("bad|be", "good", s))  # Life can good good
print(re.sub("bad|be", 'good', s, 1))  # 用“good”替换“bad”或者“be”,只替换一次         # Life can good bad
print(re.subn("bad|be", "good", s, 1))  # 用“good”替换“bad”或者“be”,只替换一次        # ('Life can good bad', 1)

r = re.subn("bad|be", "good", s)
print(r[0])  # 输出元祖第一项            # Life can good good
print(r[1])  # 输出元祖第二项               #  2
