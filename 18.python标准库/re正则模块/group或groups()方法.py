#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/15 18:15
# filename: group或groups()方法.py
import re

line = "Cats are smarter than Pigs"

matchObj = re.match(r'(.*)are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No match!!!")

'''
matchObj.group(): Cats are smarter than Pigs
matchObj.group(1): Cats 
matchObj.group(2): smarter
'''