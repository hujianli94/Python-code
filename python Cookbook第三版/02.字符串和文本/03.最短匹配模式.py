#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/29 15:46
# filename: 03.最短匹配模式.py
import re

# 贪婪匹配模式
str_pat = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

print("非贪婪模式，从而得到最短的匹配".center(100, "*"))
# 非贪婪模式，从而得到最短的匹配

str_pat = re.compile(r'"(.*?)"')
print(str_pat.findall(text2))
