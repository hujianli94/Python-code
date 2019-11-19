#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/21 18:14
# filename: json数据编码.py
import json

'''
# 准备数据
py_dic = {'name': 'hujianli', 'age': '18', 'sex': True}
py_list = [1, 3]
py_tuple = ['A', 'B', 'C']

py_dic['a'] = py_list
py_dic['b'] = py_tuple

print(py_dic)
print(type(py_dic))

# 编码过程
json_obj = json.dumps(py_dic)
print(json_obj)
print(type(json_obj))

# 编码过程
json_obj = json.dumps(py_dic, indent=4)
print(json_obj)

# 写入json数据到data1.json文件
with open('data1.json', 'w') as f:
    json.dump(py_dic, f)

# 写入json数据到data2.json文件
with open('data2.json', 'w') as f:
    json.dump(py_dic, f, indent=4)

'''


# 读取data2.json文件中的内容
with open("data2.json", 'r') as f:
    data = json.load(f)
    print(data)
