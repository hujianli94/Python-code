#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 11:09
# filename: 02.爬取淘宝商品信息.py
from selenium import webdriver
from bs4 import BeautifulSoup
import pymongo
import time
from selenium.webdriver.chrome.options import Options

# 连接mongodb
client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
taobao_rnp = mydb['taobao_renaiping']  # 连接数据库及创建数据库、数据集合


def search_good(word):
    """
    模拟淘宝搜索框搜索
    :param word:
    :return:
    """
    url = "https://www.taobao.com/"
    driver.get(url)
    driver.implicitly_wait(2)
    driver.find_element_by_id("q").clear()  # 清除搜索框内容
    # # # 先用个人账号登录淘宝
    # driver.find_element_by_id("TPL_username_1").send_keys("hujianli962057147")  # 搜索框输入用户名登录
    # driver.find_element_by_id("TPL_password_1").send_keys("cu0gu0ai@94")  # 搜索框输入密码
    # driver.find_element_by_class_name("J_Submit").click()  # 点击搜索按钮

    driver.find_element_by_id("q").send_keys(word)  # 搜索框输入搜索内容
    driver.find_element_by_class_name("btn-search").click()  # 点击搜索按钮
    return driver.current_url  # Gets the URL of the current page.


def get_info(url):
    """
    获取每一页的如下信息:
    "商品": xx
    "价格": xx
    "购买人数":xx
    "商店名称":xx
    "城市": xx
    :param url:
    :return:
    """
    driver.get(url)  # 获取网页源码
    driver.implicitly_wait(4)
    soup = BeautifulSoup(driver.page_source, "lxml")
    infos = soup.select("#mainsrp-itemlist > div > div")
    for info in infos:
        goodss = info.select("div.row > a")
        prices = info.select("div.price.g_price.g_price-highlight > strong")
        Play_Number_peoples = info.select("div.row.row-1.g-clearfix > div.deal-cnt")
        Shop_names = info.select("div.shop > a > span:nth-of-type(2)")
        Citys = info.select("div.row.row-3.g-clearfix > div.location")
        Product_links = info.select(" div.row.row-2.title > a")
        # print(Product_link)

        # goods = info.select("div.row > a")[0].get_text().strip()
        # price = info.select("div.price.g_price.g_price-highlight > strong")[0].get_text().strip()
        # Play_Number_people = info.select("div.row.row-1.g-clearfix > div.deal-cnt")[0].get_text().strip()
        # Shop_name = info.select("div.shop > a > span:nth-of-type(2)")[0].get_text().strip()
        # City = info.select("div.row.row-3.g-clearfix > div.location")[0].get_text().strip()

        for goods, price, Play_Number_people, Shop_name, City, Product_link in zip(goodss, prices, Play_Number_peoples,
                                                                                   Shop_names,
                                                                                   Citys, Product_links):
            data = {
                "商品": goods.get_text().strip(),
                "价格": price.get_text().strip(),
                "购买人数": Play_Number_people.get_text().strip(),
                "商店名称": Shop_name.get_text().strip(),
                "城市": City.get_text().strip(),
                "商品链接": "https://" + Product_link.get("href")
            }

            print(data)
            # taobao_rnp.insert_one(data)
            time.sleep(0.2)


def get_nextpage(url):
    """
    模拟鼠标进行翻页操作
    :param url:
    :return:
    """
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('a[trace="srp_bottom_pagedown"]').click()
    time.sleep(2)
    return driver.current_url


if __name__ == '__main__':

    driver = webdriver.PhantomJS()
    # driver = webdriver.Chrome()
    driver.maximize_window()

    url = search_good("篮球服")
    # print(url)
    get_info(url)

    for i in range(50):
        next_url = get_nextpage(url)
        get_info(url)
