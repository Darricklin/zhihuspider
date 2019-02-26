# -*- coding: utf-8 -*-
import scrapy
from ..items import ZhihuItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider,Rule
import re
from datetime import datetime

class TectspiderSpider(scrapy.Spider):
    name = 'tectspider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        article_list=response.xpath('')
        for article in article_list:
            item=ZhihuItem()
            item['create_time']=datetime.now()
            item['title']=article.xpath()
            item['author']=article.xpath()
            item['tag']=article.xpath()
            url=article.xpath()
            yield scrapy.Request(url=url,callback=self.next_parse,meta={'item':item},)
    def next_parse(self,response):
        item=response.meta['item']
        item['content']=response.xpath()
        print(item)
        yield item