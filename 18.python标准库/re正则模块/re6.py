#!/usr/bin/env python
#-*- coding:utf8 -*-

import re

s = '''
Life can be good;
Life can be bad;
LIfe is mostly cheerful;
But sometimes sad.
'''

r = re.compile(r'be(?=\sgood)')             #编译正则表达式，只匹配单词"good"的"be"
m = r.search(s)
print(m)                #<_sre.SRE_Match object; span=(10, 12), match='be'>

m.span()                                    #编译正则表达式，只匹配其后单词"good"的"be"
print(r.findall(s))                         #搜索字符串      #['be']
r = re.compile('be')                        #查看m
r.findall(s)

r = re.compile(r'be(?!\sgood)')
m = r.search(s)
print(m)            #<_sre.SRE_Match object; span=(28, 30), match='be'>

r = re.compile(r"(?:can\s)be(\sgood)")      #使用组来匹配"be good"
m = r.search(s)
print(m)            #<_sre.SRE_Match object; span=(6, 17), match='can be good'>
print(m.groups())   #(' good',)
print(m.group(1))   # good


r = re.compile(r'(?P<first>\w)(?P=first)')  #使用组名重复，此处匹配具有两个重复字母的单词
print(r.findall(s))                         #输出匹配到的字母       #['o', 'e']

r = re.compile(r'(?<=can\s)b\w*\b')         #匹配以字母“b”开头在“can”之后的单词
print(r.findall(s))                         #输出匹配到的单词       #['be', 'be']

r = re.compile(r"(?<!can\s)b\w*\b")         #匹配以字母"b"开头不在"can"之后单词
print(r.findall(s))         #['bad']

r = re.compile(r'(?<!can\s)(?i)b\w*\b')     #重新编译忽略大小写
print(r.findall(s))                 #['bad', 'But']





















