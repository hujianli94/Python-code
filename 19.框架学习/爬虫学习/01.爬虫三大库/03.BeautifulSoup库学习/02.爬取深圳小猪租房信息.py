#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/10 9:19
# filename: 02.爬取深圳小猪租房信息.py
import requests
from bs4 import BeautifulSoup
import time
import re
import xlwt

info_list = []  # 所有房源信息列表

urls = ["https://sz.xiaozhu.com/search-duanzufang-p{}-0/".format(str(i)) for i in range(2, 31)]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


def check_sex(class_name):
    if class_name == ["member_ico1"]:
        return "女"
    else:
        return "男"


def get_link(url):
    wb_data = requests.get(url, headers)
    soup = BeautifulSoup(wb_data.text, "lxml")
    links = soup.select("#page_list > ul > li > a")
    for link in links:
        href = link.get("href")
        get_info(href)


def get_info(url):
    """
    爬取信息如下：

    标题
    地址
    价格
    房东性别
    房东图片
    房东姓名
    房源链接地址
    :param url:
    :return:
    """
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, "lxml")
    tittles = soup.select("div.wrap.clearfix.con_bg > div > div.pho_info > h4 > em")
    address_shenzhen = soup.select("div.wrap.clearfix.con_bg > div > div.pho_info > p > span")
    price_sz = soup.select("#pricePart > div.day_l > span")
    landlord_sex = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > div")
    landlord_images = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > a > img")
    landlord_names = soup.select("#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a")
    link_address = url

    for tittle, address, price, landlord_sx, landlord_image, landlord_name in zip(tittles, address_shenzhen,
                                                                                  price_sz, landlord_sex,
                                                                                  landlord_images,
                                                                                  landlord_names):
        # data = {
        #
        #     "标题": tittle.get_text().strip(),
        #     "地址": address.get_text().strip(),
        #     "价格": price.get_text().strip(),
        #     "房东姓名": landlord_name.get_text(),
        #     "房东性别": check_sex(landlord_sx.get("class")),
        #     "房东图片": landlord_image.get("src"),
        #     "房源链接地址": link_address
        # }
        # print(data)
        landlord_info = [
            tittle.get_text().strip(), address.get_text().strip(), price.get_text().strip() + "元", landlord_name.get_text(),
            check_sex(landlord_sx.get("class")), landlord_image.get("src"), link_address
        ]
        info_list.append(landlord_info)


def save_excel(info_list, name="小猪租房信息.xls"):
    header = ["标题", "地址", "价格", "房东姓名", "房东性别", "房东图片", "房源链接"]
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




    # 单页测试
    # url = "https://sz.xiaozhu.com/search-duanzufang-p2-0/"
    # get_link(url)
    # print(info_list)
