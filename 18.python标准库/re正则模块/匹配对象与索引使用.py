#!/usr/bin/env python
#-*- coding:utf8 -*-
'''start([groupid=0])
end([groupid=0])
span([groupid=0])
'''

import re
s = '''Life can be dreams.
Life can be great thoughts;
Life can mean a person,
Sitting in a court.
'''
r = re.compile('\\b(?P<first>\w+)a(\w+)\\b')       #编译正则表达式匹配含有字母“a”的单词
m = r.search(s, 9)
print(m.start())
print(m.start(1))
print(m.start(2))
print(m.end(1))
print(m.end())
print(m.span())
print(m.span(2))
