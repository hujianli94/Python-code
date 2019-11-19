#!/usr/bin/env python
#-*- coding:utf8 -*-
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label,state)
        state +=1
    return nested

F = tester(0)
F("spam")
F("ham")
F("eggs")

print()
G = tester(42)
G('spam')
G('eggs')
G('bacon')