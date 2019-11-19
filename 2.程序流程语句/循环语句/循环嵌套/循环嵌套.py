#!/usr/bin/env python
#-*- coding:utf8 -*-


for row in range(1,5):
    if row == 2:
        print("您坐在: {}排".format(row))
        for row1 in range(11):
            if row1 == 7 :
                print("您的座位是：第{}排，第{}列".format(row,row1))
