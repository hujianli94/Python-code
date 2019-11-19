#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/8 10:40
# filename: 爬取今日头条数据.py
import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool
import re


def get_page(offset):
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "tt_webid=6734121904631956996; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6734121904631956996; csrftoken=0096bb4ab8c832a262007c79ae5d1715; s_v_web_id=be2e63799f5442a4d22deffcfc3b4918; __tasessionId=mhs8ohjjz1567994326706",
        "referer": "https://www.toutiao.com/",
        "sec-fetch-mode": "cors",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    base_url = 'https://www.toutiao.com/api/search/content/?'
    url = base_url + urlencode(params)
    # print(url)
    try:
        resp = requests.get(url, headers=headers)
        if 200 == resp.status_code:
            return resp.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('title') is None:
                continue
            title = re.sub('[\t]', '', item.get('title'))
            images = item.get('image_list')
            try:
                for image in images:
                    origin_image = re.sub("list.*?pgc-image", "large/pgc-image", image.get('url'))
                    yield {
                        'image': origin_image,
                        'title': title
                    }
            except:
                pass


def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    try:
        if not os.path.exists(img_path):
            os.makedirs(img_path)
    except:
        pass
    try:
        resp = requests.get(item.get('image'))
        if codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except Exception as e:
        print(e)


def main(offset):
    json = get_page(offset)
    # print(json)
    for item in get_images(json):
        save_image(item)


GROUP_START = 0
GROUP_END = 10

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
