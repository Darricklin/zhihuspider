# -*- coding: utf-8 -*-
import scrapy


class TectspiderSpider(scrapy.Spider):
    name = 'tectspider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
