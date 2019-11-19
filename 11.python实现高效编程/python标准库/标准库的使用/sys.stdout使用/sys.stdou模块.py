#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys
temp = sys.stdout
sys.stdout = open('log.txt', "a")
print("test")
print(1,2,3)
sys.__stdout__.close()

print("back here")
