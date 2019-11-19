#!/usr/bin/env python
#-*- coding:utf8 -*-
from collections.abc import Iterator

class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0   #初始化索引位置

    def __next__(self):
        #真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == "__main__":
    company = Company(["derek1", "derek2", "derek3"])
    my_itor = iter(company)

    print(next(my_itor))  # derek1
    print(next(my_itor))  # derek2
    print(next(my_itor))  # derek3

    print("-"*100)
    for item in company:
        print(item)