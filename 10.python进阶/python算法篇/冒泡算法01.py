#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/27 17:52
# filename: 冒泡算法01.py

def bubble_sort(nums):
    flags = True  # 循环的标志
    while flags:
        flags = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # 交换元素位置
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

                # 将标志设置为True，继续循环
                flags = True


list_test = [8, 6, 5, 3, 7, 10]
bubble_sort(list_test)
print(list_test)
