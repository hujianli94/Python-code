#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/12 16:34
# filename: 02.解析JSON库.py
import json

jsonstring = '{"user_man":[{"name":"Perter"},{"name":"xiaohu"}],' \
             '"user_woman":[{"name":"andi"},{"name":"zhangsan"}]}'


json_data = json.loads(jsonstring)
print(type(json_data))
print(json_data.get("user_man"))
print(json_data.get("user_woman"))
print(json_data.get("user_man")[0].get("name"))
print(json_data.get("user_woman")[1].get("name"))
print()
print(json_data.get("user_woman")[1]["name"])
print(json_data.get("user_man")[0]["name"])
