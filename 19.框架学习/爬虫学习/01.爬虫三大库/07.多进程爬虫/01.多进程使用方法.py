#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/15 22:11
# filename: 01.多进程使用方法.py

"""
python进行多进程爬虫使用了multiprocessing库.使用方法的代码如下：

from multiprocessing import Pool
pool = Pool(processes=4)
pool.map(func, iterable[,chunksize])

导入multiprocessing库的Pool模块
创建进程池，processes参数为设置进程的个数
利用map()函数运行进程，func参数为需运行的函数，iterable为迭代参数，可为多个URL列表进行迭代。
"""

import requests
import re
import time
from multiprocessing import Pool  # 导入多进程模块

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0"
}


def judgment(class_name):
    if class_name == "womenIcon":
        return "女"
    else:
        return "男"


def get_info(url):
    res = requests.get(url, headers=headers)
    ids = re.findall("<h2>(.*?)</h2>", res.text, re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    sexs = re.findall('<div class="articleGender (.*?)">', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i> 好笑</span>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论', res.text, re.S)
    for id, level, sex, content, laugh, comment in zip(ids, levels, sexs, contents, laughs, comments):
        info = {
            "id": id,
            "level": level,
            "sex": judgment(sex),  # 调用judgment_sex()函数
            "content": content,
            "laugh": laugh,
            "comment": comments[0]
        }
        return info


if __name__ == '__main__':
    urls = ["https://www.qiushibaike.com/text/page/{}".format(str(i)) for i in range(2, 10)]
    start_1 = time.time()
    for url in urls:
        # 单进程
        get_info(url)
    end_1 = time.time()
    print("串行爬虫，单进程:", end_1 - start_1)

    # 2个进程
    start_2 = time.time()
    pool = Pool(processes=2)
    pool.map(get_info, urls)
    end_2 = time.time()
    print("两个进程爬取：", end_2 - start_2)

    # 4个进程
    start_3 = time.time()
    pool = Pool(processes=4)
    pool.map(get_info, urls)
    end_3 = time.time()
    print("两个进程爬取：", end_3 - start_3)
