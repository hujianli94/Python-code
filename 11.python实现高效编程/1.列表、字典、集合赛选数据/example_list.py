#!/usr/bin/env python
#-*- coding:utf8 -*-
import random,timeit
#list = [1,-2,-4,5,77,8,99,-8]
data = [ random.randint(-10,10) for _ in range(10) ]  #生成-10~10之间的10个随机数
filter1 = list(filter(lambda x: x >=0, data))  #使用filter进行迭代过滤
print(filter1)

#列表解析
list_1 = [ x for x in data if x >=0 ]
print(list_1)

