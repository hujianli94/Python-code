#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/23 9:49
# filename: json模块数据解码.py
import json
#准备数据

json_obj = r'{"name":"hujianli","age":20,"sex":true,"a":[1,3],"b":["A","B","C"]}'
print(type(json_obj))

print("开始数据解码".center(100,"*"))
py_dict = json.loads(json_obj)
print(type(py_dict))
print(py_dict["name"])
print(py_dict["sex"])
print(py_dict["age"])

py_list1 = py_dict["a"]
py_list2 = py_dict["b"]
print(py_list1)
print(py_list2)


# 读取data2.json中的数据
with open("data2.json","r") as f:
    data = json.load(f)
    print(data)
    print(type(data))