#!/usr/bin/env python
#-*- coding:utf8 -*-
import re
'''
re.compile(pattern[,flags])
pattern         #正则表达式的匹配模式；
flags           #可选参数，编译标志。
'''
s = '''Life can be good;
Life can be bad;
Life is mostly cheerful;
But sometimes sad.
'''

r = re.compile("b\w*", re.I)     #编译正则表达式，忽略大小写
new = r.sub("*", s)              #使用sub()替换字符
print(new)                       #输出结果，可以看到所有以“b”开头的单词都被替换

new2 = r.sub("*", s, 2)          #只在字符串中替换两次
print(new2)

r = re.compile('b\w*')           #重新编译，不忽略大小写
new = r.subn("*", s)
print(new[0])

print(new[1])                     #输出替换的次数
new3 = r.subn("*", s, 1)          #只在字符串中替换一次



