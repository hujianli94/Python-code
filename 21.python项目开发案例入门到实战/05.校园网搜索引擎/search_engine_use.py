#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/16 9:50
# filename: search_engine_use.py
import re
import urllib
from urllib import request
from collections import deque
from bs4 import BeautifulSoup
import lxml
import sqlite3
import jieba
import math

conn = sqlite3.connect('viewsdu.db')
c = conn.cursor()
c.execute('select count(*) from doc')
N = 1 + c.fetchall()[0][0]
target = input("请输入搜索词:")
seggen = jieba.cut_for_search(target)  # 将搜索的内容分词
score = {}
for word in seggen:
    print("得到查询词：", word)
    tf = {}
    c.execute('select list from word where  term=?', (word,))
    result = c.fetchall()
    if len(result) > 0:
        doclist = result[0][0]  # 字符串“12 35 35 88 88 ”
        doclist = doclist.split(' ')
        doclist = [int(x) for x in doclist]  # ['12','35','35','88','88']
        df = len(set(doclist))  # 当前word对应的df数，去重取出
        idf = math.log(N / df)  # 计算出IDF
        print("idf:", idf)
        for num in doclist:  # 计算词频TF，即在某文档中出现的次数
            if num in tf:
                tf[num] = tf[num] + 1
            else:
                tf[num] = 1
        # TF统计结束，现在开始计算score
        for num in tf:
            if num in score:
                # 如果该num文档已经有分数了，则累加
                score[num] = score[num] + tf[num] * idf
            else:
                score[num] = tf[num] * idf

sortedlist = sorted(score.items(), key=lambda d: d[1], reverse=True)  # 对score字典按字典的值排序
# print("得分列表", sortedlist)
cnt = 0
for num, docscore in sortedlist:
    cnt += 1
    c.execute('select link from doc where id=?', (num,))  # 按照ID获取文档的连接（网址）
    url = c.fetchall()[0][0]
    print(url, "得分：", docscore)

    try:
        response = request.urlopen(url)
        content = response.read().decode('utf-8')  # 可以输出网页内容
    except:
        print("oops.....读取网页出错")
        continue

    # 解析网页输出标题
    soup = BeautifulSoup(content, 'lxml')
    title = soup.title

    if title == None:
        print("No title.")
    else:
        title = title.text
        print(title)
    if cnt > 20:
        break
if cnt == 0:
    print("无搜索结果")
