#!/usr/bin/env python
#-*- coding:utf8 -*-
import csv
with open("some.csv",'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Column1', 'Column2', 'Column3'])      #写单行
    writer.writerows([range(3) for i in range(5)])          #写多行，列表套列表
