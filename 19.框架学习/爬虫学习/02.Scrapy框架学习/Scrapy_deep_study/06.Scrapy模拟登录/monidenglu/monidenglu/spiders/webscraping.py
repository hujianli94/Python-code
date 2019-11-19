# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/profile']

    ##-------------------------------进行登录-------------------------------
    # 登录URL
    login_url = "http://example.webscraping.com/places/default/user/login"

    # 改写start_requests方法
    def start_requests(self):
        yield scrapy.Request(self.login_url, callback=self.login)

    # 登录页面的信息处理
    def login(self, response):
        form_data = {'email': '1879324764@qq.com', 'password': 'admin#123'}
        yield FormRequest.from_response(response, formdata=form_data, callback=self.parse_login)

    # 登录成功后，会自动抓取start_urls中的网址，并用parse方法解析。
    def parse_login(self, response):
        if "欢迎 jianli" in response.text:
            yield from super().start_requests()  # 继承基类的start_requests方法，处理完会自动跳转到parse方法。

    ##-------------------------------登录后-------------------------------
    # 登录后的信息解析工作
    def parse(self, response):
        keys = response.xpath('//td[@class="w2p_fl"]/label/text()').re('(.*?):')
        values = response.xpath('//td[@class="w2p_fw"]/text()').extract()
        yield dict(zip(keys, values))


# 导入CrawlerProcess类
from scrapy.crawler import CrawlerProcess

# 获取项目的设置信息
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    # 创建CrawlerProcess类对象，并将获取的设置信息传入
    process = CrawlerProcess(get_project_settings())
    # 设置需要启动的爬虫名称
    process.crawl('login')
    # 启动爬虫
    process.start()
