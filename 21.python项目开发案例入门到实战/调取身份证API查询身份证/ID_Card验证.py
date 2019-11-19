#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/25 14:03
# filename: ID_Card验证.py
import requests
import json
import pprint

key = "d3cbaa24a5ebc4e885da53e7b7f8f028"

id_card = "420981199407226517"
url = r'http://apis.juhe.cn/idcard/index?key={0}&cardno={1}'.format(key,id_card)

res = requests.get(url)
json_data = json.loads(res.text)
pprint.pprint(json_data)