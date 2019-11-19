#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/21 14:15
# filename: 03.爬取拉勾网招聘信息.py
import requests
import json
import pymongo
import time

lagouzhaopin_info = pymongo.MongoClient().mydb.lagouzhaopin_info  # 一句话即可连接到mongodb中

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "60",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_ga=GA1.2.760934632.1563690195; user_trace_token=20190721142316-0640a8f3-ab80-11e9-8134-525400f775ce; LGUID=20190721142316-0640adda-ab80-11e9-8134-525400f775ce; LG_LOGIN_USER_ID=6b3e4172f09036f2f21edff02b5274af2005ef31da845d8d; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=9f4559e6c4e9a902c11f6db340e136389a3b8df683d3d842; index_location_city=%E6%AD%A6%E6%B1%89; privacyPolicyPopup=false; JSESSIONID=ABAAABAAAGFABEF1791E42B0D54866505A3B936D2CB547D; _putrc=E546D5B1E11B0E7D; _gid=GA1.2.942116216.1563780399; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563690197,1563690958,1563780399; LGSID=20190722152641-0cb98ce8-ac52-11e9-816c-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DKkhO3fhDORmRF8L24vkjnYo1N45sTl-LVfy-uecxcFS%26wd%3D%26eqid%3Dc768fed00003ae4d000000025d35652b; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; login=true; unick=%E8%83%A1%E5%81%A5%E5%8A%9B; TG-TRACK-CODE=index_navigation; _gat=1; X_MIDDLE_TOKEN=7a58ba57a7d23b616885dc2488d9b344; X_HTTP_TOKEN=18b65e7c6a91257011618736518a9d5b613f34c0bd; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563781609; LGRID=20190722154652-de6d9969-ac54-11e9-8170-525400f775ce; SEARCH_ID=5f25e6592f7a44f187ee04aebc15f976",
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_linux%E8%BF%90%E7%BB%B4%E5%BC%80%E5%8F%91?city=%E6%AD%A6%E6%B1%89&cl=false&fromSearch=true&labelWords=&suginput=",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "X-Anit-Forge-Code": "0",
}


def get_page(url):
    params = {'first': 'true', 'pn': '1', 'kd': 'python'}
    r = requests.post(url, data=params, headers=headers)
    json_data = json.loads(r.text)
    totalcount = json_data['content']['positionResult']['totalCount']  # 获取招聘总数量
    totalpage = int(totalcount / 15)  # 获取总页数
    pagenum = totalpage if totalpage < 30 else 30  # 通过计算得到需要获取的页数，用于改变pn值。
    return pagenum


def get_info(url, params):
    r = requests.post(url, data=params, headers=headers)
    json_data = json.loads(r.text)
    results = json_data['content']['positionResult']['result']
    for result in results:
        companyId = result['companyId']
        position_name = result['positionName']
        workyear = result['workYear']
        jobNature = result['jobNature']
        financeStage = result['financeStage']
        industryField = result['industryField']
        city = result['city']
        salary = result['salary']
        positionId = result['positionId']
        positionAdvantage = result['positionAdvantage']
        companyShortName = result['companyShortName']
        district = result['district']
        createTime = result['createTime']
        companyFullName = result['companyFullName']

        info = {'公司全名': companyFullName,
                '公司简称': companyShortName,
                '城市': city,
                '地区': district,
                '职位': position_name,
                '工作年限': workyear,
                '职业性质': jobNature,
                '职业分类': industryField,
                '工资': salary,
                '公司优势': positionAdvantage}
        print(info)
        # lagouzhaopin_info.insert_one(info)


if __name__ == '__main__':
    url = "https://www.lagou.com/jobs/positionAjax.json"
    params = {
        "first": "true",
        "pn": "1",
        "kd": "linux运维开发"
    }
    pagenum = get_page(url)
    for pn in range(1, pagenum + 1):
        get_info(url, params)
        time.sleep(2)  # 记得设置睡眠时间，否则运行可能会报错。
