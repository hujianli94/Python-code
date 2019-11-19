#!/usr/bin/env python
#-*- coding:utf8 -*-
from collections import namedtuple

Student = namedtuple('Student',['name','age','sex','email'])
s = Student(name='hujianli', age=18, sex='boy', email='1879324764@qq.com')
print(s.name)
print(s.age)
print(s.sex)
print(s.email)
print()
print(isinstance(s, tuple))