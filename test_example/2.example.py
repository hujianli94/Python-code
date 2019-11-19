#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 9:38
# filename: 2.example.py
i = int(input("净利润:"))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for index in range(6):
    if i > arr[index]:
        r += (i - arr[index]) * rat[index]
        print((i-arr[index]) * rat[index])
        i = arr[index]

print(r)