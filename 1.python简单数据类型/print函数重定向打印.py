#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
file = "log2.txt"
file2 = "log.txt"
if not os.path.exists(file2):
    with open(file2,'w') as f_w:
        f_w.write("bbbb")
else:
    print("file is exists!!")

print("hujianli", file=open(file, "w"))
print("aaa", file=open(file, "a"))