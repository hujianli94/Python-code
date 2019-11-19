#!/usr/bin/env python
#-*- coding:utf8 -*-
def func(a):
    b = "spam"
    return b*a

print(func(4))
print(dir(func))
print(func.__name__)
print(func.__dict__)
print(dir(func.__code__))
print(func.__code__.co_varnames)
print(func.__code__.co_name)

print("-"*100)
func.count = 0
func.count += 1
print("func.count values:",func.count)

func.handles = 'Button-Press'
print("func.handles vlaues: " + func.handles)

