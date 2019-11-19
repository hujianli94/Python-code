#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 14:57
# filename: 02.json处理数据.py

import json

data = [{
    'name': '胡建力',
    'gender': '男',
    'birthday': '1994-07-22'
}]

# json写入数据到本地
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=4, ensure_ascii=False))

# 从文件中读取json数据

with open("data.json", 'r', encoding='utf-8') as file:
    str = file.read()
    data = json.loads(str)
    print(data)
