#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 20:39
# filename: csv文件操作.py

import csv

with open('pingan.csv', 'r') as rf:
    reader = csv.reader(rf)
    with open('pingan2.csv', 'w') as wf:
        writer = csv.writer(wf)
        headers = next(reader)
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= int(50000000):
                writer.writerow(row)
