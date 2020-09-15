import scrapy
import re
from ..items import ScraperbricksItem
import pandas as pd

class MagicSpiderSpider(scrapy.Spider):
    name = 'magic_spider'
    start_urls = ['https://www.homeonline.com/property-for-rent-new_palasiya-indore/']

    def parse(self, response):
        items = ScraperbricksItem()

        area = response.css('.cursorPointer .row+ div .row:nth-child(1) .col-sm-9::text').extract()
        price = response.css('.pricesty::text').extract()
        address = response.css('.cursorPointer > .row .col-sm-9::text').extract()
        titles = response.css('.col-md-7 h2::text').extract()

        regex = re.compile(r'[\n\r\t]')
        for i in range(len(area)):
            area[i] = regex.sub("", area[i])

        for i in range(len(price)):
            price[i] = regex.sub("", price[i])

        for i in range(len(address)):
            address[i] = regex.sub("", address[i])
        
        for i in range(len(titles)):
            titles[i] = regex.sub("", titles[i])

        items['area'] = area
        items['price'] = price
        items['address'] = address
        items['titles'] = titles

        df = pd.DataFrame.from_dict(items, orient='index')
        df.to_excel("test01.xlsx")

        yield items
        pass