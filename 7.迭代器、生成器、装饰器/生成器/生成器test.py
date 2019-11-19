#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 23:21
# filename: 生成器test.py
def square(num):
    for i in range(1, num + 1):
        yield i * i


# for i in square(5):
#     print(i, end=" ")
hujianli = square(5)
print(hujianli.__next__())
print(hujianli.__next__())
print(hujianli.__next__())
print(hujianli.__next__())
print(hujianli.__next__())
print(hujianli.__next__())
