#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 10:34
# filename: python操作Excel方法.py

import xlwt

# 定义数据表头列表
title = ["业务名称", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日", "平均流量"]

# 定义5频道一周7天的流量数据
data = [
    ["业务官网", 150, 152, 158, 149, 155, 145, 148],
    ["新闻中心", 89, 88, 95, 56, 48, 100, 99],
    ["购物频道", 200, 201, 222, 234, 180, 179, 190],
    ["体育频道", 77, 88, 99, 55, 66, 48, 90],
    ["亲子频道", 81, 82, 83, 84, 85, 86, 87],
]

# for da in data:
#     da.append(sum(da[1:])/len(da[1:]))

# 计算平均值
[da.append(sum(da[1:]) / len(da[1:])) for da in data]

book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("Sheet1")

for h in range(len(title)):
    sheet.write(0, h, title[h])

i = 1
for list in data:
    j = 0
    for data in list:
        sheet.write(i, j, data)
        j += 1
    i += 1

book.save("excel测试.xls")
