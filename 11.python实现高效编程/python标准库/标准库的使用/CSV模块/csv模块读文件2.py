#!/usr/bin/env python
#-*- coding:utf8 -*-
import csv
with open("a.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
