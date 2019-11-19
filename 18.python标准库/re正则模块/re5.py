#!/usr/bin/env python
# -*- coding:utf8 -*-
import re

s = "Phone No . 010-87654321"
r = re.compile(r'(\d+)-(\d+)')
m = r.search(s)

print(m)                    # <_sre.SRE_Match object; span=(11, 23), match='010-87654321'>
print(m.group(1))           # 010
print(m.group(2))           # 87654321
print(m.groups())           # ('010', '87654321')

r2 = re.compile(r'(?P<Area>\d+)-(?P<No>\d+)')
m = r2.search(s)
print(m)                    ##<_sre.SRE_Match object; span=(11, 23), match='010-87654321'>
print(m.groupdict(2))       # {'Area': '010', 'No': '87654321'}
print(m.group("No"))        # 87654321
print(m.group("Area"))      # 010
