#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/29 12:21
# filename: 手工抛出异常.py

def testRaise2(number):
    for i in range(number):
        try:
            if i == 2:
                raise NameError
        except NameError:
            print("Raise a NameErrot")
        print(i)
    print("end ......")

testRaise2(10)
