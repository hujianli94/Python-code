#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/13 11:25
# filename: 爬取PEXELS图片.py

"""
爬取PEXELS网站上的图片,该网站提提供海量的图片素材，图片质量很高，
https://www.pexels.com/


通过收到输入关键字，发现网页变化
https://www.pexels.com/search/book/
https://www.pexels.com/search/office/
https://www.pexels.com/search/beautiful%20girl/
https://www.pexels.com/search/girl/

可以通过API进行中文转换英文，然后构造URL
爬取图片
"""
# 导入模块
from bs4 import BeautifulSoup
import requests
import json

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

url_path = "https://www.pexels.com/search/"
word = input("输入你要下载的图片：")
url = "http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}".format(word)

res = requests.get(url)
json_data = json.loads(res.text)
translate_json_data = json_data["translateResult"][0][0]["tgt"]

url = url_path + translate_json_data + "/"  # 通过API获取英文并构造URL

# url = "https://www.pexels.com/search/book/"
wb_data = requests.get(url, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
imags = soup.select("article > a > img")
list = []
for img in imags:
    photo = img.get("src")
    list.append(photo)

path = "D:/GitHub/21_staduy_python/19.框架学习\爬虫学习/01.爬虫三大库/05.使用API/Photo_example/"


for item in list:
    data = requests.get(item, headers=headers)
    fp = open(path + item.split("?")[0][-10:], "wb")
    fp.write(data.content)      #写入图片内容
    fp.close()                  #关闭文件