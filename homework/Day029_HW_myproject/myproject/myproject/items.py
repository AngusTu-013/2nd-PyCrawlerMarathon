# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
首先在items.py內定義一些想要抓取的項目，本次爬取項目包含PTT 文章標題、文章作者、發文日期、噓推文數、內文網址等等。
'''
class PostItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    url = scrapy.Field()
    article_id = scrapy.Field()
    article_author = scrapy.Field()
    article_title = scrapy.Field()
    article_date = scrapy.Field()
    article_content = scrapy.Field()
    ip = scrapy.Field()
    message_count = scrapy.Field()
    messages = scrapy.Field()
