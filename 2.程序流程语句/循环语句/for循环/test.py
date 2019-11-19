#!/usr/bin/env python
#-*- coding:utf8 -*-
print("今有一个数，在100以内，三三数之剩余2，五五数之剩余4，七七数之剩余3，请问这个数是什么？")
for num in range(100):
    if num %3==2 and num %5 ==4 and num%7 ==3:
        print("这个数是："+ str(num))