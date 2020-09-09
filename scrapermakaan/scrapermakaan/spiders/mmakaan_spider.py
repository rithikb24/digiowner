import scrapy
from ..items import ScrapermakaanItem

import pandas as pd

class MmakaanSpiderSpider(scrapy.Spider):
    name = 'makaan_spider'
    start_urls = ['https://www.makaan.com/indore-property/geeta-bhavan-rental-flats-58662']
    page_variable = 2

    def __init__(self):
        self.items = {
            'title':[],
            'price':[],
            'area':[],
            'owner_name':[],
            'address':[]
        }

    def parse(self, response):
        
        # items = ScrapermakaanItem()
         

        area = response.css('.size .val::text').extract()
        price = response.css('.price .val::text').extract()
        title = response.css('.typelink span::text').extract()
        owner_name = response.css('.seller-name span::text').extract()
        address = response.css('.loclink strong::text').extract()

        test_title = [ ''.join(x) for x in zip(title[0::2], title[1::2], title[2::2])]

        # self.items['title'].append(test_title)
        self.items['price'].append(price)
        self.items['area'].append(area)
        # self.items['owner_name'].append(owner_name)
        # self.items['address'].append(address)
        # next_page = 'https://www.makaan.com/indore-property/mahalakshmi-nagar-rental-flats-52212?page=' +str(MmakaanSpiderSpider.page_variable) + '/'

        # if MmakaanSpiderSpider.page_variable<5:
        #     MmakaanSpiderSpider.page_variable += 1
        #     yield response.follow(next_page, callback = self.parse)

        yield self.items

        # scraped_info = {
        # 'title' : test_title,
        # 'price' : price,
        # 'area' : area,
        # 'owner_name' : owner_name,
        # 'address' : address,
        # }



        df = pd.DataFrame.from_dict(self.items, orient='index')
        # df = df.transpose()  
        df.head()
        '''lst = df['title']
        df['title'] = [ ''.join(x) for x in zip(lst[0::2], lst[1::2], lst[2::2])]'''
        df.to_excel("geetabhavan_price_area.xlsx") 


        # yield scraped_info

        # pass