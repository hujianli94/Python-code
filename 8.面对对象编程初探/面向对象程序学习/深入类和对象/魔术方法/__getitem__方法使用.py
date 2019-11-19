#!/usr/bin/env python
#-*- coding:utf8 -*-
class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        # print(self.employee[item])
        return self.employee[item]

company = Company(['11','22','33'])
a = ["derek1","derek2"]
name_set = set()

name_set.add("hujianli1")
name_set.add("hujianli2")

##extend里面可以添加任何可迭代的参数，给类添加一个魔法函数__getitem__,类就变成可迭代的，所以可以extend进去
a.extend(company)
print(a)

a.extend(name_set)
print(a)