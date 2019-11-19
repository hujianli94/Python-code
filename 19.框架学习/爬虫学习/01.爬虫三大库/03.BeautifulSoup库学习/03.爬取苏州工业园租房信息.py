#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/10 16:32
# filename: 03.爬取苏州工业园租房信息.py
import requests
import re
from bs4 import BeautifulSoup
import time
import xlwt

info_list = []  # 所有房源信息列表

header_link = "https://su.zu.ke.com"

urls = ["https://su.zu.ke.com/zufang/gongyeyuan/pg{}/?unique_id=77cc42a7-b824-4808-b574-aee7ced97554zufanggongyeyuanpg41562747636616#contentList".format(str(i)) for i in range(2,21)]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


def get_link(url):
    wb_data = requests.get(url, headers)
    soup = BeautifulSoup(wb_data.text, "lxml")
    links = soup.select(
        "#content > div.content__article > div.content__list > div > div > p.content__list--item--title.twoline > a")
    for link in links:
        href = header_link + link.get("href")
        get_info(href)


def get_info(url):
    """
    爬取信息如下：

    "标题":
    "价格":
    "租赁方式
    "空间格局
    "面积大小
    "朝向":
    "中介姓名
    "中介电话
    "发布时间
    "入住时间
    "租期":
    "看房":
    "楼层":
    "房屋链接
    :param url:
    :return:
    """
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, "lxml")
    tittles = soup.select("body > div.wrapper > div > div.content.clear.w1150 > p")
    hourse_date1 = soup.select("body > div.wrapper > div > div.content.clear.w1150 > div.content__subtitle")
    hourse_prices = soup.select("#aside > p.content__aside--title > span")
    hourse_sizes = soup.select("#aside > ul > p")
    jieshaorens = soup.select("#aside > ul > li > div.content__aside__list--title.oneline > span")
    jsr_phones = soup.select("#aside > ul > li > div.phone__hover--wrapper > p.phone__hover")
    base_infos = soup.select(
        "body > div.wrapper > div > div.content.clear.w1150 > div.content__article.fl > div.content__article__info > ul")

    hourse_link = url

    for tittle, hourse_price, hourse_size, jieshaoren, jsr_phone, base_info in zip(tittles, hourse_prices, hourse_sizes,
                                                                                   jieshaorens,
                                                                                   jsr_phones, base_infos):
        # data = {
        #
        #     "标题": tittle.get_text().strip(),
        #     "价格": hourse_price.get_text().strip() + "元/月",
        #     "租赁方式": hourse_size.get_text().split()[0],
        #     "空间格局": hourse_size.get_text().split()[1],
        #     "面积大小": hourse_size.get_text().split()[2],
        #     "朝向": hourse_size.get_text().split()[3],
        #     "中介姓名": jieshaoren.get("title"),
        #     "中介电话": jsr_phone.get_text(),
        #     "发布时间": base_info.get_text().split()[1][3:],
        #     "入住时间": base_info.get_text().split()[2][3:],
        #     "租期": base_info.get_text().split()[3][3:],
        #     "看房": base_info.get_text().split()[4][3:],
        #     "楼层": base_info.get_text().split()[5],
        #     "房屋链接": hourse_link
        #
        # }
        # print(data)
        landlord_info = [
            tittle.get_text().strip(), hourse_price.get_text().strip() + "元/月",
            hourse_size.get_text().split()[0],
            hourse_size.get_text().split()[1], hourse_size.get_text().split()[2], hourse_size.get_text().split()[3],
            jieshaoren.get("title"), jsr_phone.get_text(), base_info.get_text().split()[1][3:],
            base_info.get_text().split()[2][3:],
            base_info.get_text().split()[3][3:], base_info.get_text().split()[4][3:], base_info.get_text().split()[5],
            hourse_link
        ]
        info_list.append(landlord_info)



def save_excel(info_list, name="苏州贝壳租房信息.xls"):
    header = ["标题", "价格", "租赁方式", "空间格局", "面积大小", "朝向", "中介姓名", "中介电话", "发布时间", "入住时间", "租期", "看房", "楼层", "房屋链接"]
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("Sheet1")
    for h in range(len(header)):
        sheet.write(0, h, header[h])
    i = 1
    for list in info_list:
        j = 0
        for data in list:
            sheet.write(i, j, data)
            j += 1
        i += 1

    book.save(name)


if __name__ == '__main__':
    for url in urls:
        get_link(url)
        time.sleep(2)

    save_excel(info_list)

    ## 详细页测试
    # url = "https://su.zu.ke.com/zufang/SU2290567151528460288.html?h=SU2290567151528460288&t=default&click_position=0&nav=0&fb_expo_id=201348460213497861&unique_id=77cc42a7-b824-4808-b574-aee7ced97554zufanggongyeyuan1562741214114"
    # get_info(url)

    ## 单页测试
    # url = "https://su.zu.ke.com/zufang/gongyeyuan/pg4/?unique_id=77cc42a7-b824-4808-b574-aee7ced97554zufanggongyeyuanpg41562747698672"
    # get_link(url)
