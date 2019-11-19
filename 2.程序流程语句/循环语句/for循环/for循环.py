#!/usr/bin/env python
# -*- coding:utf8 -*-

"""

for 迭代对象 in 对象：
    循环体


#基本应用，进行数值循环

range(start, stop[, step]) -> range object
start:开始数值
stop：结束数值
step:步长

"""

'''
for i in range(1, 11, 2):
    print(i, end=" ")

for i in range(1, 11):
    print(i, end=" ")
print()

for i in range(11):
    print(i, end=" ")

'''

'''
print("计算1+2+3+4....100的结果")
result = 0  #保存累加结果的变量

for i in list(range(101)):
    result = result + i

print(result)
'''
print("今有物，不知其数，三三数之余2,五五数之余3，七七数之余2，问何物？")
for i in range(1001):
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print("答曰 这个数值是:{}".format(i))
# for循环依次迭代字符串
string1 = "不要再说我不能"
print(string1)
for ch in string1:
    print(ch)


