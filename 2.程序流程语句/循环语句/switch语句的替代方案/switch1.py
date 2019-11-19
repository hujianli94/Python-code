#!/usr/bin/env python
#-*- coding:utf8 -*-
from __future__ import division

x =1
y =2

operator = '/'

result = {
    "+": x+y,
    "-": x-y,
    "*": x*y,
    "/": x/y
}

print(result.get(operator, 'wrong value'))


def zero():
    return "zero"

def one():
    return "one"

def switch_case(value):
    switcher = {
        0: zero,
        1: one,
        2: lambda:"tow",
    }

    func = switcher.get(value, lambda :"nothing")
    return func()

print(switch_case(1))
print(switch_case(2))
print(switch_case(3))
