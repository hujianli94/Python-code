#!/usr/bin/env python
#-*- coding:utf8 -*-

"""
交集      &
并集      |
差集      -
"""

python = set(["hujianli1","hujianli2",'hujianli3','hujianli4','jianli4'])
C = set(['hujianli1','jianli1','jianli2','jianli3','jianli4'])

print("选择python学生名字:", python)
print("选择C学生的名字:", C)

print("交集运算：",python & C)       #既选择python语言又选择C语言
print("并集运算:",python | C)       #参与选课的全部学生名字
print("差集运算:",python - C)       #python语言和C语言的差集