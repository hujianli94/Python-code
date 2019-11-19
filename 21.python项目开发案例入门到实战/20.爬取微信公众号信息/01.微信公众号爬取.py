#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 22:02
# filename: 01.微信公众号爬取.py
import requests
import time
import re
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        "Cookie": "pgv_pvi=7036971008; pgv_pvid=8376803760; RK=gsA0Nej5Wd; ptcz=a45b2cd647928febb4bd92138a2b66e6c4cd97f00696c2b5b41c3c3a3ff43c21; tvfe_boss_uuid=c17a6b75b136bd41; ua_id=ZiClGTuoX6pmRCEnAAAAAMxW3T1hhLxwKh2XiPTfcUA=; mm_lang=zh_CN; o_cookie=1879324764; uuid=af5a7895234d154c64c6780aae52381e; bizuin=3215417856; ticket=7b3bc1192ad15763b0852fa47c25edb3a46e7649; ticket_id=gh_656f0f56229d; cert=A_FKA2CRdKHYxoVbjYLI10HHTQwoKYVh; noticeLoginFlag=1; pgv_si=s6668625920; rewardsn=; wxtokenkey=777",
        "Host": "mp.weixin.qq.com",
        "Origin": "https://mp.weixin.qq.com",
        "Referer": "https://mp.weixin.qq.com/s/ZkgerJQY1NFAno2_J9PEgQ",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    except:
        print("request高级用法 error")


def get_weixin_info(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")
    wenxi_tittle = soup.select('#activity-name')[0]
    wx_title = wenxi_tittle.get_text().strip()
    IS_yuanchuang = soup.select('#meta_content span')[0].get_text().strip()
    author = soup.select('#meta_content span')[1].get_text().strip()
    wx_gongzhonghao_author_info = soup.select('#meta_content span')[2].get_text().strip()
    wx_Article_infos = soup.select("#js_content p ")
    with open(wx_title + ".txt", "w", encoding="utf-8") as f:
        f.write(wx_title + "\n")
        f.write(IS_yuanchuang + "\n")
        f.write(author + "\n")
        f.write(wx_gongzhonghao_author_info + "\n")
        f.write("\n")
        for info in wx_Article_infos:
            f.write(info.get_text().strip() + "\n")


if __name__ == '__main__':
    # url = "https://mp.weixin.qq.com/s/ZkgerJQY1NFAno2_J9PEgQ"
    # url = "https://mp.weixin.qq.com/s/xOn7T3j-Mrc639Pvw3dGKA"
    # get_weixin_info(url)
    url_info_list = ["https://mp.weixin.qq.com/s/ZkgerJQY1NFAno2_J9PEgQ",
                     "https://mp.weixin.qq.com/s/xOn7T3j-Mrc639Pvw3dGKA",
                     "https://mp.weixin.qq.com/s/_GOQUX4_VHhgipVgjQcp_A",
                     "https://mp.weixin.qq.com/s/2roSIJKen6VXwkdG84d2aA",
                     "https://mp.weixin.qq.com/s/YIi2Sts5buld8AJpAnI_fw",
                     "https://mp.weixin.qq.com/s/E8XG7G_lFO72U6CqXaDF7w",
                     "https://mp.weixin.qq.com/s/4gCyg0ld88SgcEmWNp8ahg",
                     "https://mp.weixin.qq.com/s/nb3CA8x8ArFSdEVTiChJ8w"]
    for url in url_info_list:
        get_weixin_info(url)