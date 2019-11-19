# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ChinanewsCrawlerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()  # 标题
    link = Field()  # 新闻详情链接
    desc = Field()  # 新闻综述
    pub_date = Field()  # 发布日期
