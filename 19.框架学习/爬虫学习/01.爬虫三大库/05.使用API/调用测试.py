#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/12 21:52
# filename: 调用测试.py
import requests
import json
import pprint

"""
shop_name = input("请输入商品名称：")
url = "http://suggest.taobao.com/sug?code=utf-8&q={}&callback=cb".format(shop_name)
res = requests.get(url)
res = res.text.replace("cb(", "").replace(")", "")
json_data = json.loads(res)
pprint.pprint(json_data)ae17f16ecb87ff3f76e87695ae709496
"""

caipu_name = input("请输入菜谱名称：")
key = "ae17f16ecb87ff3f76e87695ae709496"
url = "http://apis.juhe.cn/cook/query?key={0}&menu={1}&rn=2&pn=3".format(key, caipu_name)
res = requests.get(url)
json_data = json.loads(res.text)
print(json_data)
# pprint.pprint(json_data)
#
# # 写入json数据
# with open("西红柿鸡蛋汤.json", "w", encoding="utf-8") as f:
#     json.dump(json_data, f, indent=4, ensure_ascii=False)
