#!/usr/bin/env python
#-*- coding:utf8 -*-
def coffee(*coffeename):
    print("\n我喜欢的咖啡有:")
    for item in coffeename:
        print(item)

coffee("蓝山")
coffee("蓝山","卡布奇洛","巴西")


list1 = ["蓝山", "卡布奇洛", "巴西"]
coffee(*list1)  #解包用法
