#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/13 11:13
# filename: 03.调用api接口查询全国天气.py
import requests
import json
import pprint

key = "91536efa9a578f9b33318278dc711eb5"
city_weather = input("请输入查询的城市：")
url = "http://v.juhe.cn/weather/index?format=2&cityname={0}&key={1}".format(city_weather, key)

res = requests.get(url)
json_data = json.loads(res.text)
print(type(json_data))

# with open("武汉天气.json", "w", encoding="utf-8") as f:
#     json.dump(json_data, f, ensure_ascii=False, indent=4)
#
# with open("武汉天气.json", "r", encoding="utf-8") as f:
#     json_info = json.load(f)
#     print(json_info)
