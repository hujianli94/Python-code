#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
filename = "hujianli.txt"
if os.path.exists(filename):
    print("file is exists...")
else:
    f = open(filename,"w")
    f.write("this is test file!")
    f.close()

print(os.path.exists(filename))
print(os.path.exists("test"))
print(os.path.exists("."))
print(os.path.exists(".."))
