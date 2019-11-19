#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/25 13:44
# filename: 调取身份证查询API.py
import random
import requests
import json
import pprint
import time

All_ID_Card = []

key = "d3cbaa24a5ebc4e885da53e7b7f8f028"

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ID_card = "4220219930119"

for i in range(5000):
    id = random.sample(num_list, 4)
    id = [str(i) for i in id]
    id_str = "".join(id)
    ID_card_sfz = ID_card + id_str
    All_ID_Card.append(ID_card_sfz)


def Check_id_Card(ID_card):
    url = r'http://apis.juhe.cn/idcard/index?key={0}&cardno={1}'.format(key, ID_card)
    res = requests.get(url)
    json_data = json.loads(res.text)
    pprint.pprint(json_data)

    # 写入json数据
    # with open("身份证信息.json", "a", encoding="utf-8") as f:
    #     json.dump(json_data, f, indent=4, ensure_ascii=False)


# Check_id_Card("422202199107226219")

for id_card in All_ID_Card:
    Check_id_Card(id_card)
    time.sleep(0.5)
