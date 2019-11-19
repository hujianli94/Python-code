#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 14:29
# filename: translate.py
from urllib import request
from urllib import parse
import json
import hashlib

def translate_Word(en_str):
    URL = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    # en_ter = input("请输入要翻译的内容：")
    # 创建字典
    # Form_data = {"from": "en",
    #              "to": "zh",
    #              "q": en_str,
    #              "appid": "xxxxxxxxx",
    #              "salt": "xxxxxxxx"}

    From_data = {}
    From_data["from"] = "en"
    From_data["to"] = "zh"
    From_data["q"] = en_str
    From_data["appid"] = "20190701000313439"
    From_data["salt"] = '1435660288'
    Key = "_49o4XDpcC0UOwTNp4ss"

    m = From_data["appid"] + en_str + From_data["salt"] + Key

    m_MD5 = hashlib.md5(m.encode("utf8"))
    From_data["sign"] = m_MD5.hexdigest()

    data = parse.urlencode(From_data).encode("utf-8")
    # print(data)

    response = request.urlopen(URL, data)  # 传递Request对象和转换完格式的数据
    html = response.read().decode("utf-8")  # 读取信息并解码
    translate_results = json.loads(html)  # 使用JSON
    # print(json.dumps(translate_results, indent=4, sort_keys=True, ensure_ascii=False))  # 打印出JSON数据
    translate_results = translate_results["trans_result"][0]["dst"]
    print("翻译的结果是：{}".format(translate_results))
    return translate_results






