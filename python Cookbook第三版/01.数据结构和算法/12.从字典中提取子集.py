#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 20:00
# filename: 12.从字典中提取子集.py

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {key: value for key, value in prices.items() if value > 20}

tech_names = {"AAPL", "IBM", "HPQ", "MSFT"}
p2 = {key: value for key, value in prices.items() if key in tech_names}

print(p1)
print("分割线".center(100, "*"))
print(p2)
