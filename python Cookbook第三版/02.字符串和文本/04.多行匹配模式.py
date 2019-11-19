#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/29 15:53
# filename: 04.多行匹配模式.py
import re

text1 = '/* this  is a comment */'
text2 = '''/* this is a
multiline comment */
'''

comment = re.compile(r'/\*(.*?)\*/')
print(comment.findall(text1))
print(comment.findall(text2))

comment = re.compile(r'/\*(.*?)\*/', re.S)
# comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)

print(comment.findall(text2))
