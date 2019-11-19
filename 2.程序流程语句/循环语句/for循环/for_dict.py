#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 15:29
# filename: for_dict.py
my_dict = {"语文": 89, "数学": 99, "英文": 80}

print("------------------------------------------------------------")
print("通过items()方法遍历所有的key-value对")
# 通过items()方法遍历所有的key-value对
for key, value in my_dict.items():
    print("key:{}".format(key), "------------>", "value:{}".format(value))


print("------------------------------------------------------------")
print("通过keys()来遍历所有的key")
#通过keys()来遍历所有的key
for key in my_dict.keys():
    print("key:{}".format(key), "------------>", "value:{}".format(my_dict[key]))


print("------------------------------------------------------------")
print("通过values()来遍历所有的key")
#通过keys()来遍历所有的key
for value in my_dict.values():
    print("value:{}".format(value))



for key in my_dict:
    print("key:{}".format(key))
else:
    print("for循环结束.....")
