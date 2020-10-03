import scrapy
from ..items import ScrapermakaanItem

import pandas as pd

area_list, price_list, title_list, owner_name_list, address_list, furnishing_list, links = [],[],[],[],[],[], []

class MmakaanSpiderSpider(scrapy.Spider):
    name = 'makaan_spider'
    page_number = 2
    start_urls = ['https://www.makaan.com/listings?postedBy=owner&sortBy=date-desc&listingType=rent&pageType=LISTINGS_PROPERTY_URLS&cityName=Pune&localityName=wakad&suburbName=PCMC&cityId=21&localityId=50118&suburbId=10244&templateId=MAKAAN_LOCALITY_LISTING_RENT&page=1']

    def parse(self, response):
        
        items = ScrapermakaanItem()

        area = response.css('.size .val::text').extract()
        price = response.css('.price .val::text').extract()
        title = response.css('.typelink span::text').extract()
        owner_name = response.css('.seller-name span::text').extract()
        address = response.css('.loclink strong::text').extract()
        furnishing = response.css('.w44 .val::text').extract()
        link = response.xpath('//a[@class="typelink"]/@href').extract()

        test_title = [ ''.join(x) for x in zip(title[0::3], title[1::3], title[2::3])]

        area_list.extend(area)
        price_list.extend(price)
        title_list.extend(test_title)
        owner_name_list.extend(owner_name)
        address_list.extend(address)
        furnishing_list.extend(furnishing)
        links.extend(link)

        items['title'] = title_list
        items['price'] = price_list
        items['area'] = area_list
        items['owner_name'] = owner_name_list
        items['address'] = address_list
        items['furnishing'] = furnishing_list
        items['links'] = link


        # scraped_info = {
        # 'title' : test_title,
        # 'price' : price,
        # 'area' : area,
        # 'owner_name' : owner_name,
        # 'address' : address,
        # }

        yield items

        next_page = 'https://www.makaan.com/listings?postedBy=owner&sortBy=date-desc&listingType=rent&pageType=LISTINGS_PROPERTY_URLS&cityName=Pune&localityName=wakad&suburbName=PCMC&cityId=21&localityId=50118&suburbId=10244&templateId=MAKAAN_LOCALITY_LISTING_RENT&page='+ str(MmakaanSpiderSpider.page_number) + '/'
        if MmakaanSpiderSpider.page_number<10:
            MmakaanSpiderSpider.page_number += 1
            yield scrapy.Request(url = next_page, callback = self.parse)




        df = pd.DataFrame.from_dict(items, orient='index')
        df = df.transpose()  
        # df.head()
        # '''lst = df['title']
        # df['title'] = [ ''.join(x) for x in zip(lst[0::2], lst[1::2], lst[2::2])]'''
        df.to_excel("pune02.xlsx")



        pass