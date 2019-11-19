#!/usr/bin/env python
#-*- coding:utf8 -*-
f = open("hujianli_bak1.py","r",encoding="utf8")
while True:
    line = f.readline().strip()
    if not line:
        break
    print(line)
