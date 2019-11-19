#!/usr/bin/env python
# -*- coding:utf8 -*-

# 快速生成列表，根据某个列表生成满足需要的列表
import random  # 导入生成随机数的模块

list1 = []  # 定义一个空列表
for i in range(10):
    list1.append(random.randint(10, 100))  # 向列表中添加随机数
print(list1)

list1 = [random.randint(10, 100) for i in range(10)]
print(list1)

print("偶数的平方".center(100, "="))
# 偶数平方的列表，10以内的2的平方
list2 = [i * i for i in range(2, 11, 2)]
print(list2)

price = [1000, 500, 800, 888, 666]
sale = [int(x / 2) for x in price]
# sale = [int(x*0.5) for x in price]
print(sale)

# 求偶数
list3 = [i for i in range(11) if i % 2 == 0]
print(list3)

# 求基数
list3 = [i for i in range(11) if i % 2 == 1]
print(list3)

# 筛选
list3 = [i for i in range(11) if 4 < i < 10]
print(list3)

print("分割线".center(100, "*"))
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)
odd_list = list(map(lambda i: i * i, odd_list))
print(odd_list)

print("=" * 100)
squmber = [x ** 2 for x in range(20)]
print(squmber)

print("=" * 100)
# 去掉列表中元素前后的空格
mybag = [" hujianli", "  apple", "green leaf "]
mybag_after = [str(x).strip() for x in mybag]
print(mybag_after)

# 找出0~99之间能被5整除的数
number = [x for x in range(100) if x % 5 == 0]
print(number)

print("***************奇数+1，偶数不变*********************8")
tuple_example = (1, 2, 3, 4, 5, 6, 7, 8, 9)
exam1 = [x if x % 2 == 0 else x + 1 for x in tuple_example]
print(exam1)
