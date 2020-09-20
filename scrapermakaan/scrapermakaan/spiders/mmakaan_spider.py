import scrapy
from ..items import ScrapermakaanItem

import pandas as pd

class MmakaanSpiderSpider(scrapy.Spider):
    name = 'makaan_spider'
    page_number = 2
    start_urls = ['https://www.makaan.com/listings?propertyType=apartment&postedBy=owner&listingType=rent&pageType=LOCALITY_URLS&cityName=Indore&localityName=vijay%20nagar&suburbName=Indore%20North&cityId=13&localityId=52245&suburbId=10286&templateId=MAKAAN_LOCALITY_LISTING_RENT']

    def parse(self, response):
        
        items = ScrapermakaanItem()

        area = response.css('.size .val::text').extract()
        price = response.css('.price .val::text').extract()
        title = response.css('.typelink span::text').extract()
        owner_name = response.css('.seller-name span::text').extract()
        address = response.css('.loclink strong::text').extract()

        test_title = [ ''.join(x) for x in zip(title[0::3], title[1::3], title[2::3])]


        items['title'] = test_title
        items['price'] = price
        items['area'] = area
        items['owner_name'] = owner_name
        items['address'] = address


        # scraped_info = {
        # 'title' : test_title,
        # 'price' : price,
        # 'area' : area,
        # 'owner_name' : owner_name,
        # 'address' : address,
        # }

        yield items

        # next_page = 'https://www.makaan.com/indore-residential-property/rent-property-in-indore-city?page='+ str(MmakaanSpiderSpider.page_number) + '/'
        # if MmakaanSpiderSpider.page_number<10:
        #     yield response.follow(next_page, callback = self.parse)




        df = pd.DataFrame.from_dict(items, orient='index')
        df = df.transpose()  
        # df.head()
        # '''lst = df['title']
        # df['title'] = [ ''.join(x) for x in zip(lst[0::2], lst[1::2], lst[2::2])]'''
        df.to_excel("final.xlsx")



        pass