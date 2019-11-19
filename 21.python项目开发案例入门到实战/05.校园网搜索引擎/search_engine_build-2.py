#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/15 11:18
# filename: search_engine_build-2.py
import sys
from collections import deque
import urllib
from urllib import request
import re
from bs4 import BeautifulSoup
import lxml
import sqlite3
import jieba

base_url = "https://www.zut.edu.cn"
url = 'https://www.zut.edu.cn/index/xwdt.htm'  # 入口

unvisited = deque()  # 待爬取链接的集合，使用广度优先搜索
visited = set()  # 已访问的链接集合
unvisited.append(url)

conn = sqlite3.connect("viewsdu.db")
c = conn.cursor()

# 在建表之前先drop table。
c.execute('drop table doc')
c.execute('create table doc(id int primary key ,link text)')
c.execute('drop table word')
c.execute('create table word(term varchar (25) primary key ,list text)')
conn.commit()
conn.close()


print("开始爬取".center(50, "*"))
cnt = 0

info = """

                          .-""-.
                         (___/\ \
       ,                 (|^ ^ ) )
      /(                _)_\=_/  (
,..__/ `\          ____(_/_ ` \   ) 
 `\    _/        _/---._/(_)_  `\ (
   '--\ `-.__..-'    /.    (_), |  ) 
       `._        ___\_____.'_| |__/
         `~----"`    `-.........'
"""


print("(●_●)开始爬取【{}】(●︿●).......".format(base_url))
print(info)
print()
print("开始爬取".center(50, "*"))



while unvisited:
    url = unvisited.popleft()
    visited.add(url)
    cnt += 1
    # 读取队列信息进行爬取
    print("开始抓取第", cnt, '个链接:', url)

    # 爬取网页内容
    try:
        response = request.urlopen(url)
        content = response.read().decode('utf-8')
    except:
        continue

    soup = BeautifulSoup(content, 'lxml')
    all_a = soup.find_all('a', {'class': 'c67214'})  # 本页面所有的新闻链接 <a>

    for a in all_a:
        x = a['href']
        if re.match(r'http.+', x):
            if not re.match(r'http\:\/\/www\/zut\.edu\.cn/.+', x):
                continue
        if re.match(r'\/info\/.+', x):
            x = base_url + x

        if re.match(r'info/.+', x):
            x = base_url + "/" + x

        if re.match(r'\.\.\/info/.+', x):
            x = base_url + x[2:]

        if re.match(r'\.\.\/\.\.\/info/.+', x):
            x = base_url + x[5:]
        # print(x)
        if (x not in visited) and (x not in unvisited):
            unvisited.append(x)

    a = soup.find('a', {'class': 'Next'})  # 下一页<a>

    if a != None:
        x = a['href']
        if re.match(r'xwdt\/.+', x):  # 检测翻页字段
            x = base_url + "/" + 'index/' + x  # 拼接翻页地址
        else:
            x = base_url + "/index/xwdt/" + x
        print("开始翻页------>", x)
        if (x not in visited) and (x not in unvisited):
            unvisited.append(x)

    title = soup.title
    article = soup.find('div', class_="c67215_content", id='vsb_newscontent')  # 内容
    author = soup.find('span', class_='authorstyle67215')  # 作者
    time = soup.find('span', class_='timestyle67215')  # 发布时间

    if title == None and article == None and author == None:
        print("无内容页面。")
        continue
    elif article == None and author == None:
        print("只有标题.")
        title = title.text
        title = ''.join(title.split())
        article = ''
        author = ''

    elif article == None:
        print("有标题和作者,内容缺失.")
        title = title.text
        title = ''.join(title.split())
        article = ''
        author = author.get_text("", strip=True)
        author = "".join(author.split())

    elif author == None:
        print("有标题和内容.缺失作者")
        title = title.text
        title = ''.join(title.split())
        article = article.get_text("", strip=True)
        article = "".join(author.split())
        author = ''
    else:
        title = title.text
        title = ''.join(title.split())
        article = article.get_text("", strip=True)
        article = "".join(str(author).split())
        author = author.get_text("", strip=True)
        author = "".join(author.split())

    print("网页标题:", title)

    seggen = jieba.cut_for_search(title)
    seglist = list(seggen)
    seggen = jieba.cut_for_search(article)
    seglist += list(seggen)
    seggen = jieba.cut_for_search(author)
    seglist += list(seggen)

    # 数据存储
    conn = sqlite3.connect("viewsdu.db")
    c = conn.cursor()
    c.execute('insert into doc values (?,?)', (cnt, url))

    # 对每个分出的词语建立倒排词表
    for word in seglist:
        # print(word)
        # 检测看看这个词语是否已存在于数据库
        c.execute('select list from word where term=?', (word,))
        result = c.fetchall()
        # 如果不存在
        if len(result) == 0:
            docliststr = str(cnt)
            c.execute('insert into word values (?,?)', (word, docliststr))
        # 如果已经存在
        else:
            docliststr = result[0][0]  # 得到字符串
            docliststr += ' ' + str(cnt)
            c.execute('update word set list=? where term=?', (docliststr, word))
    conn.commit()
    conn.close()
    print("词表建立完毕！！！")