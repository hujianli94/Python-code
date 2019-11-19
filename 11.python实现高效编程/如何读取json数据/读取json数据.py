#!/usr/bin/env python
#-*- coding:utf8 -*-
import json

with open("date.json","r") as f:
    date = json.load(f)
print(date)

print("读取序列化文件".center(100, "*"))
hu = json.load(open("db", "r"))
print(hu)
# print(type(hu))