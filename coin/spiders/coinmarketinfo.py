# -*- coding: utf-8 -*-
import scrapy
from coin.items import CoinItem


class CoinmarketinfoSpider(scrapy.Spider):
	name = 'coinmarketinfo'
	allowed_domains = ['coinmarketcap.com']
	start_urls = ['http://coinmarketcap.com/all/views/all']

	def parse(self, response):
		tbody_lists = response.xpath("//tbody/tr")
		item = CoinItem()
		for tbody_list in tbody_lists:
			rank = tbody_list.xpath("./td[1]/text()").extract_first()
			name = tbody_list.xpath("./td[2]/a/text()").extract_first()
			symbol = tbody_list.xpath("./td[2]/span/a/text()").extract_first()
			market = tbody_list.xpath("./td[4]/text()").extract_first()
			price = tbody_list.xpath("./td[5]/a/text()").extract_first()
			circulating = tbody_list.xpath("./td[6]/span/text()").extract_first()
			valume = tbody_list.xpath("./td[7]/a/text()").extract_first()
			value_1 = tbody_list.xpath("./td[8]/text()").extract_first()
			value_24 = tbody_list.xpath("./td[9]/text()").extract_first()
			value_7 = tbody_list.xpath("./td[10]/text()").extract_first()
			link = tbody_list.xpath("./td[2]/span/a/@href").extract_first()

			item["Rank"] = rank
			item["Name"] = name
			item["Symbol"] = symbol
			item["Market_Cap"] = market
			item["Price"] = price
			item["Circulating_Supply"] = circulating
			item["Volume"] = valume
			item["value1"] = value_1
			item["value2"] = value_24
			item["value3"] = value_7
			item["Link"] = link
			
			yield item
