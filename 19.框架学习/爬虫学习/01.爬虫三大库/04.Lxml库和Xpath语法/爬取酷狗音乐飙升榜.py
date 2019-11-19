#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/10 23:45
# filename: 爬取酷狗音乐飙升榜.py
import requests
from bs4 import BeautifulSoup
import time
import re
from lxml import etree

"""
使用3种方式爬取酷狗音乐的飙升榜

"""

url = "https://www.kugou.com/yy/html/rank.html"


def get_html(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    except:
        print("request高级用法 error")


def Re_serach(url):
    """
    使用re正则抓取酷狗音乐
    :param url:
    :return:
    """
    html_info = get_html(url)
    info1 = re.compile('<li class=" " title="(.*?)">')
    music_html = re.compile('<a href="(.*?)" data-active="playDwn" data-index="\d"')
    music_info_all = info1.findall(html_info, re.S)
    music_songs = music_html.findall(html_info, re.S)
    for music, music_song in zip(music_info_all, music_songs):
        info = {
            "歌曲排名:": str(music).split("data-index=\"")[1],
            "歌名": str(music).split("data-index=\"")[0],
            "播放链接：": music_song
        }
        print(info)


def Beautifulsoup_search(url):
    """
    使用Beautifulsoup抓取酷狗
    :param url:
    :return:
    """
    html_info = get_html(url)
    soup = BeautifulSoup(html_info, "lxml")
    song_ids = soup.select("#rankWrap > div.pc_temp_songlist.pc_rank_songlist_short > ul > li > a")
    # print(song_ids)
    # song_ids = soup.select("#rankWrap > div.pc_temp_songlist.pc_rank_songlist_short > ul > li > a")
    # song_id = re.findall("\"\d\"", str(song_id))
    song_names = soup.select("#rankWrap > div.pc_temp_songlist.pc_rank_songlist_short > ul > li > a")
    URL_songs = soup.select("#rankWrap > div.pc_temp_songlist.pc_rank_songlist_short > ul > li > a")

    for song_id, song_name, URL_song in zip(song_ids, song_names, URL_songs):
        data = {
            "歌曲排行": int(song_id.get("data-index")) + 1,
            "歌曲名称": song_name.get_text().strip(),
            "歌曲链接": URL_song.get("href")
        }
        print(data)


def Xapth_select(url):
    html = get_html(url)
    selector = etree.HTML(html)
    url_infos = selector.xpath('//*[@id="rankWrap"]/div[2]')
    for urlinfo in url_infos:
        song_names = urlinfo.xpath('ul/li/a/text()')
        ids = urlinfo.xpath('ul/li/span[3][@ class="pc_temp_num"]/text()')
        ids = [str(id).strip("\t").strip("\r").strip("\n").strip() for id in ids]
        idss = [id for id in ids if id]
        song_links = urlinfo.xpath('ul/li/a/@href')

        for songnam, id, song_link in zip(song_names, idss, song_links):
            data = {
                "歌曲名称": songnam,
                "歌曲排名": int(id) - 3,
                "歌曲链接": song_link
            }
            print(data)


if __name__ == '__main__':
    # Re_serach(url)
    # Beautifulsoup_search(url)
    Xapth_select(url)


