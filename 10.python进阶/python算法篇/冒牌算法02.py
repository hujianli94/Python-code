#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 9:11
# filename: 冒牌算法02.py

# 冒牌排序
def bubbleSort(num):
    for j in range(len(num) - 1, -1, -1):
        for i in range(j):
            if num[i] > num[i + 1]:  # 把数值小的数字放到顶端
                num[i], num[i + 1] = num[i + 1], num[i]
            print(num)


def main():
    numbers = [10, 8, 7, 11, 29, 7]
    bubbleSort(numbers)


if __name__ == '__main__':
    main()