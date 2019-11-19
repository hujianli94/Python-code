#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 15:05
# filename: 03.csv文件存储.py

# 写入
import csv

with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile:
    wirter = csv.writer(csvfile)
    wirter.writerow(['id', 'name', 'age'])
    wirter.writerow(['10001', 'Mike', '20'])
    wirter.writerow(['10002', 'Bob', '22'])
    wirter.writerow(['10003', 'Jordan', '21'])

# 写入csv文件中文乱码的解决
with open("name01.csv", "w", newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["胡建力", "吴明", "胡慧"])
    w.writerow(["吴明", "胡慧", "胡建力"])

# 字典写入
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},

        {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},

        {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
        ]

with open('stocks.csv', 'w', newline='', encoding='utf-8') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

# csv文件读取
with open('stocks.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 使用pandas的read_csv()方法
import pandas as pd

df = pd.read_csv('stocks.csv')
print(df)
