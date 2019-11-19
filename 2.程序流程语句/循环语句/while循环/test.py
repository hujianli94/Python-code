#!/usr/bin/env python
#-*- coding:utf8 -*-
num = 100
count = 0
print("今有一个数，在100以内，三三数之剩余2，五五数之剩余4，七七数之剩余3，请问这个数是什么？")
while count <= num:
    if count %3==2 and count %5 ==4 and count%7 ==3:
        print("这个数是："+ str(count))
    count +=1
print("循环结束！！".center(100, "-"))