import scrapy
from ..items import ScrapermakaanItem

import pandas as pd

class MmakaanSpiderSpider(scrapy.Spider):
    name = 'makaan_spider'
    start_urls = ['https://www.makaan.com/indore-residential-property/rent-property-in-indore-city?page=1']
    page_variable = 2

    def parse(self, response):
        
        items = ScrapermakaanItem()
         

        area = response.css('.size .val::text').extract()
        price = response.css('.price .val::text').extract()
        title = response.css('.typelink span::text').extract()
        owner_name = response.css('.seller-name span::text').extract()
        address = response.css('.loclink strong::text').extract()

        test_title = [ ''.join(x) for x in zip(title[0::2], title[1::2], title[2::2])]


        items['title'] = test_title
        items['price'] = price
        items['area'] = area
        items['owner_name'] = owner_name
        items['address'] = address
        next_page = 'https://www.makaan.com/indore-residential-property/rent-property-in-indore-city?page=' +str(MmakaanSpiderSpider.page_variable) + '/'

        if MmakaanSpiderSpider.page_variable<10:
            MmakaanSpiderSpider.page_variable += 1
            yield response.follow(next_page, callback = self.parse)

        yield items

        # scraped_info = {
        # 'title' : test_title,
        # 'price' : price,
        # 'area' : area,
        # 'owner_name' : owner_name,
        # 'address' : address,
        # }



        # df = pd.DataFrame.from_dict(scraped_info, orient='index')
        # df.transpose()  
        # df.head()
        # '''lst = df['title']
        # df['title'] = [ ''.join(x) for x in zip(lst[0::2], lst[1::2], lst[2::2])]'''
        # df.to_excel("demo.xlsx")


        # yield scraped_info

        # pass