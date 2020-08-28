# -*- coding: utf-8 -*-
import scrapy
from ..items import ScraperbricksItem

class MagicSpiderSpider(scrapy.Spider):
    name = 'magic_spider'
    start_urls = ['https://www.homeonline.com/property-for-rent-new_palasiya-indore/']

    def parse(self, response):
        items = ScraperbricksItem()

        area = response.css('.cursorPointer .row+ div .row:nth-child(1) .col-sm-9::text').extract()
        price = response.css('.pricesty::text').extract()
        address = response.css('.cursorPointer > .row .col-sm-9::text').extract()

        for p in price:
            p = p.replace('\n', '')
            p = p.replace('\t', '')
            p = p.replace('\r', '')

        items['price'] = price

        yield price

        pass