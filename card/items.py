# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CardItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    head_time = scrapy.Field()
    head_type = scrapy.Field()
    head_tnover = scrapy.Field()
    head_balance = scrapy.Field()

    bodys= scrapy.Field()

    body_time = scrapy.Field()
    body_type = scrapy.Field()
    body_tnover = scrapy.Field()
    body_balance = scrapy.Field()
