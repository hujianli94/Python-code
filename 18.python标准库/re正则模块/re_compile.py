#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/21 17:43
# filename: re_compile.py
import re

p = r'\w+@hujianli\.com'
regex = re.compile(p)

text = "Tony's email is tony_187@hujianli.com"
m = regex.search(text)
print(m)

m = regex.match(text)
print(m)

p = r"[Jj]ava"
regex = re.compile(p)
text = 'I like Java and java'
match_list = regex.findall(text)
print(match_list)

match_iter = regex.finditer(text)
for m in match_iter:
    print(m.group())

p = r'\d+'
regex = re.compile(p)
text = 'AB1234QCD34EF'

clist = regex.split(text)
print(clist)

repace_text = regex.sub("-",text)
print(repace_text)