# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MatplotlibExamplesPipeline(object):
    def process_item(self, item, spider):
        return item


from scrapy.pipelines.files import FilesPipeline
import os


class MyFilesPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        folder = request.url.split('/')[-2]
        filename = request.url.split('/')[-1]
        return os.path.join(folder, filename)
