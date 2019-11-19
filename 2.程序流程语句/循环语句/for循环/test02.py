#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 15:22
# filename: test02.py
s_max = input("请输入您想计算的阶乘：")
mx = int(s_max)
result = 1

# 还有for-in循环遍历范围
for num in range(1, mx + 1):
    result = result * num
print(result)
