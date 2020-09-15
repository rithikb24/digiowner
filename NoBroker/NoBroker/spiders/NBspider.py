import scrapy
import pandas as pd


class NBSpider(scrapy.Spider):
    name = 'nb_spider'
    start_urls = [
        'https://www.nobroker.in/property/rent/mumbai/Navi%20Mumbai/?searchParam=W3sibGF0IjoxOS4wMzMwNDg4LCJsb24iOjczLjAyOTY2MjUsInBsYWNlSWQiOiJDaElKclJNZnVQQzU1enNSYWZpRkVXajNFanciLCJwbGFjZU5hbWUiOiJOYXZpIE11bWJhaSJ9XQ==&sharedAccomodation=0&orderBy=nbRank,desc&radius=2&traffic=true&travelTime=30&propertyType=rent&pageNo=10'
    ]

    def __init__(self):
            self.items = {
                'title':[],
                'price':[],
                'area':[],
                # 'owner_name':[],
                'address':[]
            }

    def parse(self, response):              
        title = response.css('h2::text').extract()
        price = response.css('.solid-border-right .inr_resale+ span::text').extract()
        area = response.css('.solid-border-right meta+ span::text').extract()
        # owner_name = response.css('.seller-name span::text').extract()
        address = response.css('.card-header-title h5::text').extract()

        # TO REMOVE UNWANTED SYMBOLS AND DATA
        for i, elem in enumerate(title):
             title[i] = elem.replace('\n', '') 

        for i, elem in enumerate(address):
             address[i] = elem.replace('\n', '') 


        self.items['title'].append(title)
        self.items['price'].append(price)
        self.items['area'].append(area)
        self.items['address'].append(address)

        yield self.items

        df = pd.DataFrame() 
        df = pd.DataFrame.from_dict(self.items, orient='index')
        df = df.transpose()	
        df.to_excel('r1.xlsx')

        # df = pd.DataFrame() 
        # df = pd.DataFrame.from_dict(self.items, orient='index')
		# # df.transpose()	
		# # df.head()
		# df.to_excel('r.xlsx', index = False)

		
        pass