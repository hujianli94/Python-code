#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/13 14:07
# filename: 使用有道翻译的api.py

import requests
import json
import pprint

translate = input("请要翻译的词语：")
url = "http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}".format(translate)

res = requests.get(url)
json_data = json.loads(res.text)
translate_json_data = json_data["translateResult"][0][0]["tgt"]

with open("翻译.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

with open("data.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(json_data, indent=4, ensure_ascii=False))

with open("翻译.json", "r", encoding="utf-8") as f:
    json_info = json.load(f)
    print(translate_json_data)
