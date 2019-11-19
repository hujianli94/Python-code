#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/10 20:38
# filename: 01.使用re爬取斗破苍穹小说.py
"""

手动浏览网页前5章如下：
http://www.doupoxs.com/doupocangqiong/1.html
http://www.doupoxs.com/doupocangqiong/2.html
http://www.doupoxs.com/doupocangqiong/3.html
http://www.doupoxs.com/doupocangqiong/4.html
http://www.doupoxs.com/doupocangqiong/5.html
"""

import requests
import re
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"

}

f = open("doupo.txt", 'a+')


def get_info(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:  # 判断请求码是否为200
        contents = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'), re.S)    #匹配包括换行在内的所有字符，匹配多于p标签
        for content in contents:
            f.write(content + "\n")     #正则获取数据写入TXT文件中
    else:
        pass            # 不为200就pass掉


if __name__ == '__main__':  # 程序主入口
    #构造多页url
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2, 500)]  # 构造多页url
    # print(urls)
    for url in urls:
        get_info(url)  # 循环调用get_info()函数
        time.sleep(1)  #休眠1秒

f.close()  # 关闭txt文件
