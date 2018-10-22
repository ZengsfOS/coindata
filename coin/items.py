#-*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	Rank = scrapy.Field()
	Name = scrapy.Field()
	Symbol = scrapy.Field()
	Market_Cap = scrapy.Field()
	Price = scrapy.Field()
	Circulating_Supply = scrapy.Field()
	Volume = scrapy.Field()
	value1 = scrapy.Field()
	value2 = scrapy.Field()
	value3 = scrapy.Field()
	Link = scrapy.Field()
