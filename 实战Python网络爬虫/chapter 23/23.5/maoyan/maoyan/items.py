# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class MaoyanItem(scrapy.Item):
    movieName = scrapy.Field()
    performer = scrapy.Field()
    releasetime = scrapy.Field()
    score = scrapy.Field()
    pass
