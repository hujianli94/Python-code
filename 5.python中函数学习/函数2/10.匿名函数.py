#!/usr/bin/env python
# -*- coding:utf8 -*-
# 计算圆面积的函数
import math

result = lambda r: math.pi * r * r
r = 10
print(result(r))

# result1 = lambda [arg1,[arg2,....argn] : expression

bookinfo = [('不一样的卡梅拉', 22.50, 120), ('零基础学Android', 65.10, 85), ('摆渡人', 23.40, 130), ('福尔摩斯探案', 20.50, 110)]
print('爬取到的商品名称:\n', bookinfo, '\n')
bookinfo.sort(key=lambda x: (x[1], x[1] / x[2]))  # 指定排序规则
print('排序后的商品信息: \n', bookinfo, '\n')
