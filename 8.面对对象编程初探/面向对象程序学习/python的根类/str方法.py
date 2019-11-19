#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/18 8:10
# filename: str方法.py
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        template = "Person [name={0},age={1}]"
        s = template.format(self.name, self.age)
        return s


person = Person("hujianli", 18)
print(person)