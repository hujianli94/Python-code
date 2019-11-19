#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/23 9:43
# filename: json模块编码.py
import json

py_dict = {"name": "hujianli", "age": 18, "sex": True}
py_list = [1, 3]
py_tuple = ("A", "B", "C")

py_dict["a"] = py_list
py_dict["b"] = py_tuple
print(py_dict)
print(type(py_dict))

# 编码过程
json_obj = json.dumps(py_dict)
print(json_obj)
print(type(json_obj))

# 编码过程，使用格式化输出
json_obj = json.dumps(py_dict, indent=4)
# 输出格式化后的字符串
print(json_obj)
print(type(json_obj))

# 写入json数据到data1.json文件
with open('data1.json', 'w') as f:
    json.dump(py_dict, f)

# 写入json数据到data2.json文件
with open('data2.json', 'w') as f:
    json.dump(py_dict, f, indent=4)



# 读取data2.json文件中的内容
with open("data2.json", 'r') as f:
    data = json.load(f)
    print(data)
