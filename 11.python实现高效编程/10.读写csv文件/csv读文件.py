#!/usr/bin/env python
#-*- coding:utf8 -*-
import csv
'''
with open("some.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
'''
'''
with open("villains",'rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin if row]
print(villains)
'''
'''
with open("villains","rt") as fin:
    cin = csv.DictReader(fin,fieldnames=["first","last"])
    villains = [row for row in cin]

print(villains)
'''
with open("villains", "rt") as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin if row]
print(villains)


















