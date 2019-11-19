#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
任何定义了__enter__()方法和__exit__()方法的对象都可以用于上下文管理器。
'''

class Vow(object):
    def __init__(self, text):               #构造函数，text为传入参数
        self.text = text

    def __enter__(self):
        self.text = "I say: " + self.text       #增加前缀,实例化类之后的操作
        return self                             #返回一个对象
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.text = self.text + "!"              #增加后缀，类调用完毕之后的操作
        print(self.text)

with Vow("I'm hujianli") as myVow:
    print(myVow.text)