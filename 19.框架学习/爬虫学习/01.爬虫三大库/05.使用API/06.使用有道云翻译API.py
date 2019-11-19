#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/9 17:50
# filename: 06.使用有道云翻译API.py
import requests
import json


def translate_date(world=None):
    url = 'http://fanyi.youdao.com/translate'

    Form_data = {
        'i': world,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15653441929319',
        'sign': 'e06b85ab13b925e8a0fd85383c85e9b8',
        'ts': '1565344192931',
        'bv': '53539dde41bde18f4a71bb075fcf2e66',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

    response = requests.post(url, data=Form_data)
    content = json.loads(response.text)
    print(content['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    translate_date("运维开发")
