#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/22 18:46
# filename: CSV数据交换格式-读.py

# reader()函数  读
import csv

with open("test.csv", "r", encoding="utf-8") as rf:
    reader = csv.reader(rf, dialect=csv.excel)
    for row in reader:
        print("|".join(row))
