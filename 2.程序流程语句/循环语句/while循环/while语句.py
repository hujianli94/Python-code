#!/usr/bin/env python
#-*- coding:utf8 -*-


'''
while 条件表达式：
    循环体
    不满足条件表达式时，自动跳出循环
'''

number = 500           #定义范围
start_nu = 0            #计数器

while start_nu <= number:
    if start_nu%3 == 2 and start_nu%5 == 3 and start_nu%7 == 2:
        print("答曰 这个数值是:{}".format(start_nu))
    start_nu +=1
print("循环结束！！")
