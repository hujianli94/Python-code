#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/16 17:11
# filename: 调用阿里云api发送短信.py

import urllib.request
import urllib3
from urllib import parse


def getClient():
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    return http


querys = {
    'ParamString': {"name": "肖先生"},  # 消息体参数
    'RecNum': '18515555555,13917777777',  # 手机号码，用逗号隔开
    'SignName': 'Python科技',  # 短信签名名称
    'TemplateCode': 'SMS_33465621'  # 短信模板编号
}
querys = parse.urlencode(querys)
host = 'http://sms.market.alicloudapi.com'
path = '/singleSendSms'
method = 'GET'
appcode = '2d1d*****49484eb*****cdf24974f1945'
bodys = {}
url = host + path + '?' + querys
req = urllib.request.Request(url)
header = {'Authorization': 'APPCODE ' + appcode}
req = getClient().request('GET', url, headers=header)