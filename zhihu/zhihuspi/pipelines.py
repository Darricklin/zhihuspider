# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


# class ZhihuPipeline(object):
#     def process_item(self, item, spider):
#         return item

class ZhihuMysqlPipeline(object):
    def open_spider(self, object):
        self.connect = pymysql.connect(
            host='140.143.232.130',
            user='root',
            password='123456',
            port='3306',
            db='zhihubbs',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        sql = "insert into posts values (0,'%s','%s','%s','%s','%s')" % (
        item['create_time'], item['title'], item['content'], item['tag'],
        item['author'])
        self.cursor.execute(sql)
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.connect.close()
        self.cursor.close()
