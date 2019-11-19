#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/10 9:44
# filename: 冒泡排序03.py
import time


def maopao_sort(num):
    for i in range(len(num)):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
            else:
                continue
    print(num)


if __name__ == '__main__':
    list1 = [4, 2, 1, 17, 112, 233, 344, 22, 13, 56, 88, 20]
    start_time = time.clock()
    maopao_sort(list1)
    end_time = time.clock()
    print("耗时：{}".format((end_time - start_time) / 60))
