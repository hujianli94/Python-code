#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/15 16:08
# filename: __del__ 析构方法.py

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __del__(self):
        print("del删除对象")


if __name__ == '__main__':
    im = Item("鼠标", 29.8)
    # x = im

    #打印im所引用的Item对象
    del im
    print("------------------------------")
