#!/usr/bin/env python
#-*- coding:utf8 -*-
print([ x+y for x in "yes" for y in "no" ])

list2 = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(list2)

'''
[line.rstrip() for line in open('myfile').readlines()] ['aaa', 'bbb', 'ccc']
[line.rstrip() for line in open('myfile')] ['aaa', 'bbb', 'ccc']
list(map((lambda line: line.rstrip()), open('myfile'))) ['aaa', 'bbb', 'ccc']
'''