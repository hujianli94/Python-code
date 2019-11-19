#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/9 17:43
# filename: 爬取武汉蔡甸地区短租信息.py
import requests
from bs4 import BeautifulSoup
import re
import xlwt

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

info_list_excel = []  # 放置信息的列表，转为列表为放入Excel中


def GetHous_price(url):
    """
    :param url:
    :return: 区域、小区名称、房屋面积、几室几厅、价格
    """

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    regions = soup.select(
        "#content > div.content__article > div.content__list > div > div > p.content__list--item--des > a:nth-of-type(2)")
    xiaoqu_names = soup.select(
        "#content > div.content__article > div.content__list > div > div > p.content__list--item--des > a:nth-of-type(3)")
    House_area = soup.select(
        "#content > div.content__article > div.content__list > div > div > p.content__list--item--des ")
    House_area = re.findall(".*㎡", str(House_area))
    areas = [area.strip() for area in House_area]
    pattern = soup.select(
        "#content > div.content__article > div.content__list > div > div > p.content__list--item--des")
    pattern = re.findall("\d室\d厅\d卫", str(pattern))
    pattern_infos = [pattern_info.strip() for pattern_info in pattern]
    prices = soup.select("#content > div.content__article > div.content__list > div > div > span > em")
    for i in range(len(pattern_infos)):
        for region, xiaoqu_name, area, pattern_info, price in zip(regions, xiaoqu_names, areas, pattern_infos, prices):
            # info = {
            #     "蔡甸区域": region.get_text(),
            #     "小区名称": xiaoqu_name.get_text(),
            #     "房屋面积": area,
            #     "格局": pattern_info,
            #     "租房价格": price.get_text() + "元"
            # }
            info = [
                region.get_text(), xiaoqu_name.get_text(), area, pattern_info, price.get_text() + "元"

            ]
            info_list_excel.append(info)


# url = "https://wh.zu.ke.com/zufang/caidian/pg2l1/?unique_id=77cc42a7-b824-4808-b574-aee7ced97554zufangcaidianpg2l11562666447973"
urls = [
    "https://wh.zu.ke.com/zufang/caidian/pg{}l1/?unique_id=77cc42a7-b824-4808-b574-aee7ced97554zufangcaidianpg2l11562666146987#contentList".format(
        str(i)) for i in range(2, 12)]
#
for url in urls:
    GetHous_price(url)
# content > div.content__article > div.content__list > div:nth-child(1) > div > p.content__list--item--des > a:nth-child(2)
# #content > div.content__article > div.content__list > div:nth-child(1) > div > p.content__list--item--des > a:nth-child(3)

# GetHous_price(url)
# print(len(info_list))
# for House_list in info_list_excel:
#     print(House_list)

header = ["蔡甸区域", "小区名称", "房屋面积", "格局", "租房价格"]
book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("Sheet1")
for h in range(len(header)):
    sheet.write(0, h, header[h])
i = 1
for list in info_list_excel:
    j = 0
    for data in list:
        sheet.write(i, j, data)
        j += 1
    i += 1

book.save("zufang.xls")
