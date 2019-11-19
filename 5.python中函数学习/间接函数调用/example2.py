#!/usr/bin/env python
#-*- coding:utf8 -*-
def echo(message):
    print(message)

s = [(echo,'hujianli学习'),(echo,"xiaojian爱吃肉")]
for (func, arg) in s:
    func(arg)

