#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
通过2个方法实现迭代
iter()
next()
'''
string = "hujianli"
it = iter(string)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
'''
while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)
'''

class Fibs:
    def __init__(self, n=10):
        self.a = 0
        self.b = 1
        self.n = n      #定义初始化参数n

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b, self.a + self.b     #a=b b=a+b
        if self.a > self.n:         #退出条件
            raise StopIteration
        return self.a,self.b

hu = Fibs(100)
for i in hu:
    print(i)