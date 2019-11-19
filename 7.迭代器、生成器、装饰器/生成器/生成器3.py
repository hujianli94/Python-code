#!/usr/bin/env python
# -*- coding:utf8 -*-

def squre(input):
    for num in range(input):
        print("before yied..")
        yield num * num
        print("after yield..")



for num in squre(4):
    print(num)

