#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/23 14:49
# filename: 04.模拟登陆实战 - 爬取微博信息.py
import requests
import json

url = "https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=filter_type%3Drealtimehot%26mi_cid%3D100103%26pos%3D0_0%26c_type%3D30%26display_time%3D1563868912&luicode=10000011&lfid=231583"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "cookie": "_T_WM=58715283899; WEIBOCN_FROM=1110006030; ALF=1566456408; MLOGIN=1; SCF=AhBeVPx74kSl5qF6iY4voqvEHfFIQnvmhzl4WihTqODrKh2_bM9sx1tB7_pSJziQqFxzTkvYpPibbSO3Ai3tFfQ.; SUB=_2A25wMt0JDeRhGeNI6lQV-CvLzDqIHXVT3ONBrDV6PUJbktANLWelkW1NSIopRGQYg7Z67DMZ4I7Fb9wbAQ86cGz_; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWrrugNpckdSZHXoaF_iBBy5JpX5K-hUgL.Fo-ceKqX1h-NS0q2dJLoI0YLxK-LBo5L12qLxKqLBo-LBoMLxKML1-zL1KMLxKML1-2L1hBLxK-L12qLBKeLxK.LBKeL12-LxKML1K5LBoBt; SUHB=0pHxAFsEBBWmE9; SSOLoginState=1563864409; XSRF-TOKEN=8a0666; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231583%26fid%3D106003type%253D25%2526t%253D3%2526disable_hot%253D1%2526filter_type%253Drealtimehot%26uicode%3D10000011"
}

r = requests.get(url, headers=headers)
json_data = json.loads(r.text)
# print(json.dumps(json_data, indent=4, sort_keys=False, ensure_ascii=False))  ##结构化json数据

hot_groups = json_data['data']['cards'][0]["card_group"]
realtime_groups = json_data['data']['cards'][1]['card_group']


# print(json.dumps(realtime_groups, indent=4, sort_keys=False, ensure_ascii=False))

with open("weibo.txt", "w", encoding="utf-8") as f:
    for hot_group in hot_groups:
        text1 = hot_group["desc"]
        f.write(text1 + "\n")

    for relaltime_group in realtime_groups:
        text2 = relaltime_group["desc"]
        f.write(text2 + "\n")

