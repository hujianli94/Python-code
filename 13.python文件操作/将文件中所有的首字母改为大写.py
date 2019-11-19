#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 12:38
# filename: 将文件中所有的首字母改为大写.py

with open("foo_bak_01.txt") as inf, open('out.txt', 'w') as outf:
    for line in inf:
        outf.write(' '.join([word.capitalize() for word in line.split()]))
        outf.write('\n')
