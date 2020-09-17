import scrapy
import pandas as pd


class MBSpider(scrapy.Spider):
    name = 'mb_spider'
    start_urls = [
        'https://www.magicbricks.com/property-for-rent/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&Locality=Vijay-Nagar&cityName=Indore'
    ]

    # def __init__(self):
    #         self.items = {
    #             'title':[],
    #             'price':[],
    #             'area':[],
    #             'owner_name':[],
    #             'address':[]
    #         }

    def parse(self, response):              
        title = response.css('h2::text').extract()
        price = response.css('.solid-border-right .inr_resale+ span::text').extract()
        area = response.css('.solid-border-right meta+ span::text').extract()
        # owner_name = response.css('.seller-name span::text').extract()
        address = response.css('.card-header-title h5::text').extract()

        # TO REMOVE UNWANTED SYMBOLS AND DATA
        # for i, elem in enumerate(title):
        #      title[i] = elem.replace('\n', '') 

        # for i, elem in enumerate(address):
        #      address[i] = elem.replace('\n', '') 


        self.items['title'].append(title)
        self.items['price'].append(price)
        self.items['area'].append(area)
        self.items['address'].append(address)

        yield self.items

        # df = pd.DataFrame() 
        # df = pd.DataFrame.from_dict(self.items, orient='index')
        # df = df.transpose()	
        # df.to_excel('r2.xlsx')
		
        pass