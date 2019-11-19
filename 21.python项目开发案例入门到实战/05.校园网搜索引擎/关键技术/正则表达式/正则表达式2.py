#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/12 16:53
# filename: 正则表达式2.py
import re

t = '19:05:25'
m = re.match(r'^(\d\d)\:(\d\d)\:(\d\d)$', t)  # r原义
print("m.string:", m.string)  # m.string: 19:05:25

print(m.re)  # re.compile('^(\\d\\d)\\:(\\d\\d)\\:(\\d\\d)$')
print("m.pos:", m.pos)  # m.pos: 0
print("m.endpos:", m.endpos)  # m.endpos: 8
print("m.lastindex:", m.lastindex)  # m.lastindex: 3
print("m.lastgroup:", m.lastgroup)  # m.lastgroup: None
print("m.group(0):", m.group(0))  # m.group(0): 19:05:25
print("m.group(1,2):", m.group(1, 2))  # m.group(1,2): ('19', '05')
print("m.groups():", m.groups())  # m.groups(): ('19', '05', '25')
print("m.groupdict():", m.groupdict())  # m.groupdict(): {}
print("m.start(2):", m.start(2))  # m.start(2): 3
print("m.end(2):", m.end(2))  # m.end(2): 5
print("m.span:", m.span(2))  # m.span: (3, 5)
