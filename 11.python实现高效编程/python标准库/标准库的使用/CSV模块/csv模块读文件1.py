#!/usr/bin/env python
#-*- coding:utf8 -*-
import csv
list = csv.reader(open("a.csv"))
for line in list:
    print(line)