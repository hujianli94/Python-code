#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/9 18:39
# filename: test10.py
# list = ['                  105㎡', '                  90㎡', '                  81㎡', '                  81㎡',
#         '                  78㎡', '                  87㎡', '                  87㎡', '                  87㎡',
#         '                  85㎡', '                  71㎡', '                  65㎡', '                  77㎡',
#         '                  87㎡', '                  80㎡', '                  43㎡', '                  87㎡',
#         '                  90㎡', '                  90㎡', '                  76㎡', '                  84㎡',
#         '                  89㎡', '                  87㎡', '                  85㎡', '                  100㎡',
#         '                  43㎡', '                  81㎡', '                  90㎡', '                  75㎡',
#         '                  91㎡', '                  85㎡']
#
# list2 = [i.strip() for i in list]
# print(list2)


# import re
# r = re.compile("[1-9]\d*.\d*|0\.\d*[1-9]\d*")
# string = '[<span class="x_textscore">4.8<em class="f_24">/5分</em></span>]'
# s = r.findall(string)
# print(s)
import requests
from bs4 import BeautifulSoup

h = {
    "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

a = requests.get("https://www.kugou.com/yy/html/rank.html")
soup = BeautifulSoup(a.text,"lxml")
song_name = soup.select("#rankWrap > div.pc_temp_songlist.pc_rank_songlist_short > ul > li > a")
print(song_name)
