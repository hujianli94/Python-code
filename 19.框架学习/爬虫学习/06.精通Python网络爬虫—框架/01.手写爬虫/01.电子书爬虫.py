#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/19 15:53
# filename: 01.图片爬虫实战.py
'''
翻页信息
http://www.xz577.com/e/python/2.html
http://www.xz577.com/e/python/3.html
http://www.xz577.com/e/python/4.html
http://www.xz577.com/e/python/5.html
http://www.xz577.com/e/python/6.html

'''

import re
import urllib
from urllib import request
import os
import time


class Book_spider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
        }
        self.start_page = 2
        self.start = 0
        self.title_html = "http://www.xz577.com"
        self.html = "http://www.xz577.com/e/python/"
        self.path = os.path.abspath(os.path.dirname(os.path.basename(__file__)))

    def get_books_info(self):
        try:
            url = self.html + str(self.start_page) + ".html"
            req = request.Request(url, headers=self.headers)
            response = request.urlopen(req)
            page = response.read().decode('utf-8')
            self.start += 1
            return page
        except Exception as e:
            print(print("抓取失败，失败原因:{}".format(e)))

    def get_image_down(self):
        html = self.get_books_info()
        print("正在获取第{}页数据".format(self.start))
        print("------------------------------------------------------------------------------------------")
        print("爬取的网站是: {}".format(self.html + str(self.start_page) + ".html"))
        print("------------------------------------------------------------------------------------------")
        print()
        pat1 = '<a href=(.*?) title=(.*?)target="_blank">.*?</a>'
        pat2 = '<img src=(.*?) alt=.*?>'
        result1 = re.compile(pat1).findall(html, re.S)
        result2 = re.compile(pat2).findall(html, re.S)

        links = []
        books_name = []
        book_path = []

        for i in result1:
            link = self.title_html + i[0].strip("\"")
            book_name = i[1]

            links.append(link)
            books_name.append(book_name)

        for name in books_name:
            file_dir_name = self.path + "/" + str(name).replace("\"", '')
            book_path.append(file_dir_name)

        # print(books_name)

        for path, photo_link, book_name, link in zip(book_path, result2, books_name, links):
            try:
                if not os.path.exists(path):
                    os.mkdir(path)
            except:
                pass
            image_jpg_name = str(path).strip() + "/" + str(path).split('/')[1].strip() + '.jpg'
            photo_link = str(photo_link).replace("\"", '').strip()
            # # print("正在下载:{!r} 【图片下载地址】：{!r}".format(image_jpg_name, photo_link))
            # # print("书籍名称:{!r}  下载链接：{!r}".format(book_name, link))
            try:
                urllib.request.urlretrieve(photo_link, image_jpg_name)
            except Exception as e:
                print(e)

            path_book_txt = str(path).strip() + "/" + str(path).split('/')[1].strip() + '.txt'
            try:
                with open(path_book_txt, 'w', encoding="utf-8") as f:
                    f.write("书籍名称：{!r}\n下载链接地址：{!r}".format(book_name, link))
            except:
                pass

    def main(self):
        while self.start < 5:
            self.get_image_down()
            self.start_page += 1
            time.sleep(1)


if __name__ == '__main__':
    t1 = Book_spider()
    t1.main()
