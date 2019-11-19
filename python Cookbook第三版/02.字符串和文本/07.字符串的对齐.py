#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/30 9:58
# filename: 07.字符串的对齐.py
text = 'Hello World'
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '=>20s'))
print(format(text, '*^20s'))
print()
print(text.rjust(20, "="))
print(text.center(20, "*"))

print("{:>10s}{:>10s}".format("Hello", "World"))

x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))
