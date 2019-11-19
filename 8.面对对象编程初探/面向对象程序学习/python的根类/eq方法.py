#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/18 8:14
# filename: eq方法.py

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        template = "Person [name={0},age={1}]"
        s = template.format(self.name, self.age)
        return s

    def __eq__(self, other):
        if self.age == other.age and self.name == other.name:
            return True
        else:
            return False


person1 = Person("hujianli", 18)
person2 = Person("hujianli", 18)
print(person1 == person2)

