# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshumongodbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author_url = scrapy.Field()
    new_article = scrapy.Field()
    author_name = scrapy.Field()
    focus = scrapy.Field()
    fans = scrapy.Field()
    article_num = scrapy.Field()
    write_num = scrapy.Field()
    like_num = scrapy.Field()
