#!/usr/bin/env python
#-*- coding:utf8 -*-

#推导式可以快速生成字典
'''
{键表达式：值表达式 for 循环}
'''
import random
#生成随机数字典，键为1~4，值为10~100的随机数
randomdict = {i: random.randint(10,100) for i in range(1,5)}
print(randomdict)

name = ["依梦","冷依依","香菱","戴兰"]
sign = ["水瓶","射手","双鱼","双子"]
dict1 = {i:j for i,j in zip(name,sign)}
print(dict1)