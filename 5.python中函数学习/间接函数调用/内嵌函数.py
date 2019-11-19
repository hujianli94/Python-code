#!/usr/bin/env python
#-*- coding:utf8 -*-
def foo():
    print("in the foo")
    def bar():
        print("in the bar name:{}")
    return bar

foo()
foo()()

