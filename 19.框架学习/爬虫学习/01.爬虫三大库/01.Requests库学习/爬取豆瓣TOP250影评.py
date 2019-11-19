#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/18 14:09
# filename: 爬取豆瓣TOP250影评.py
from urllib import request
import re
import json

"""
翻页查看
https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
"""


class MovieTop(object):
    def __init__(self):
        self.start = 0
        self.param = '&filter='
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        self.move_list = []
        self.file_path = "./movie_spider.txt"

    def get_page(self):
        """
        获取页数
        :return:
        """
        try:
            url = "https://movie.douban.com/top250?start={}".format(self.start)
            req = request.Request(url, headers=self.headers)
            response = request.urlopen(req)
            page = response.read().decode('utf-8')
            page_num = (self.start + 25) // 25
            print("正则抓取{}页数据....".format(page_num))
            self.start += 25
            return page
        except request.URLError as e:
            if hasattr(e, 'reason'):
                print("抓取失败，失败原因:{}".format(e.reason))

    def get_movie_info(self):
        pattern = re.compile(
            '<div class="item">.*?<span class="title">(.*?)</span>.*?<span class="other">&nbsp;/&nbsp;(.*?)</span>.*?<span class="playable">(.*?)</span>.*?<p class="">(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span>(.*?)</span>.*?<span class="inq">(.*?)</span>',
            re.S)

        while self.start <= 225:
            html = self.get_page()
            moves_info = re.findall(pattern, html)
            for info in moves_info:
                Movie_name = info[0]
                Keyword = info[1]
                isPlay = info[2]
                info_yanyuan = str(info[3]).strip()
                score = info[4]
                number_of_People = info[5]
                Summary = info[6]
                self.move_list.append([Movie_name, Keyword, isPlay, info_yanyuan, score, number_of_People, Summary])

    def write_text(self):
        print("开始向文件写入数据....................")
        File_top = open(self.file_path, "w", encoding='utf-8')
        try:
            for movie in self.move_list:
                File_top.write("电影名称：" + movie[0] + "\r\n")
                File_top.write("电影关键词：" + movie[1] + "\r\n")
                File_top.write("是否可播放：" + movie[2] + "\r\n")
                File_top.write("导演/演员信息：" + movie[3] + "\r\n")
                File_top.write("电影评分：" + movie[4] + "\r\n")
                File_top.write("评论人数：" + movie[5] + "\r\n")
                File_top.write("电影精髓：" + movie[6] + "\r\n")
            print("抓取结果写入文件成功.........")
        except Exception as e:
            print(e)
        finally:
            File_top.close()

    def main(self):
        print("开始从豆瓣电影抓取数据....................")
        self.get_movie_info()
        self.write_text()
        print("数据抓取完毕.............")


if __name__ == '__main__':
    t1 = MovieTop()
    t1.main()
