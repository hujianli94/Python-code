#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/18 17:31
# filename: class_urls.py
'''
爬取地址：https://wh.58.com/sale.shtml
爬取信息：标题，价格，区域，浏览量，想买数，宝贝描述内容，宝贝留言数
爬取方式：进入分类的详细页面，使用lxml解析。
存储方式：MongoDB存储 & MySQL存储


进入分类页面，以二手手机为例。分类链接为http://gz.58.com//shouji/，
点击多页后发现该类别的个人分类规律为：http://gz.58.com//shouji/0/pn{}/，其中{}放置数字即可实现翻页。


'''

import requests
from lxml import etree

start_url = "http://cs.58.com/sale.shtml"
base_url = "http://cs.58.com"

r = requests.get(start_url)
html = etree.HTML(r.text)
infos = html.xpath('//li[@class="ym-tab"]')
for info in infos:
    urls = info.xpath('span/a/@href')        ##简单二级目录
    #urls = info.xpath('ul/li/span/a/@href') ##复杂二级目录
    for url in urls:
        class_url = base_url + url
        print(class_url)


class_urls1 = '''
http://cs.58.com/shouji/
http://cs.58.com/tongxunyw/
http://cs.58.com/danche/
http://cs.58.com/diandongche/
http://cs.58.com/diannao/
http://cs.58.com/shuma/
http://cs.58.com/jiadian/
http://cs.58.com/ershoujiaju/
http://cs.58.com/yingyou/
http://cs.58.com/fushi/
http://cs.58.com/meirong/
http://cs.58.com/yishu/
http://cs.58.com/tushu/
http://cs.58.com/wenti/
http://cs.58.com/kaquan/
http://cs.58.com/shebei.shtml
http://cs.58.com/chengren/
'''
