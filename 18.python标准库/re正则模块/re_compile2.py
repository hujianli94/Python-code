#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/21 17:54
# filename: re_compile2.py
import re

text = "你们好Hello"

p = r"\w+"
regex = re.compile(p, re.U)

m = regex.search(text)
print(m)            #匹配

m1 = regex.match(text)
print(m1)            #匹配


regex = re.compile(p, re.A)
m = regex.search(text)
print(m)            #匹配


regex = re.compile(p, re.A)
m = regex.match(text)
print(m)        #不匹配
