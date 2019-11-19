#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 12:31
# filename: 06.用列表推导式来取代map和filter.py
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x ** 2 for x in a]
squares1 = [x ** 2 for x in a if x % 2 == 0]
print(squares)
print(squares1)

# 使用map实现
squares2 = list(map(lambda x: x ** 2, a))
print(squares2)

# 使用map和filter实现
squares3 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a)))
print(squares3)

"""
1.列表推导式要比内置的map和filter函数清晰，因为它无需额外编写lambda表达式
2.列表推导式可以跳过输入列表中的某些元素，如果改用map来做，那就必须辅以filter方能实现
3.字典和集合也支持推导表达式
"""
