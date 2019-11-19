#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/10/28 14:57
# filename: 选择排序.py

def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positonOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positonOfMax]:
                positonOfMax = location

        alist[fillslot], alist[positonOfMax] = alist[positonOfMax], alist[fillslot]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

selectionSort(alist)
print(alist)