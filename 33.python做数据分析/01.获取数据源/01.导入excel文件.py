#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/31 12:42
# filename: 01.导入excel文件.py
import pandas as pd

# 导入.xlsx文件
df = pd.read_excel(r'chart.xlsx')
df1 = pd.read_excel(r'chart.xlsx', sheetname='Sheet1', usecols=[0, 2], header=1)
print(df)
print()
print(df1)

# df2 = pd.read_excel(r'D:/21-DAY-Python/33.python做数据分析/2019云腾技术部技_张少锋个人.xlsx', sheetname='张少锋 详情')
# print(df2)
