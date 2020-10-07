import scrapy
import pandas as pd
import re
from ..items import MagicbricksItem

class MBSpider(scrapy.Spider):
    name = 'mb_spider'
    start_urls = [
        'https://www.magicbricks.com/property-for-rent/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&Locality=Dewas-Naka&cityName=Indore'
    ]
    # ]
    

    # def __init__(self):
    #         items = {
    #             'title':[],
    #             'price':[],
    #             'area':[],
    #             'owner':[]
    #             # 'owner_name':[],
    #             # 'address':[]
    #         }

    def parse(self, response):  

        items = MagicbricksItem()    

        # images = response.css('.lazy , .m-srp-card__summary__item:nth-child(2) .m-srp-card__summary__info::text').extract()
        title = response.css('.m-srp-card__title::text').extract()
        price = response.css('.m-srp-card__price::text').extract()
        area = response.css('input+ .m-srp-card__summary__item .m-srp-card__summary__info::text').extract() # Not every property have area in it's title
        owner = response.css('.m-srp-card__advertiser__name::text').extract()
        # furnishing = response.css('.m-srp-card__summary__item:nth-child(2) .m-srp-card__summary__info::text').extract()
        posted_date = response.css('.m-srp-card__post-date span::text').extract()
        # owner_name = response.css('.seller-name span::text').extract()
        # address = response.css('.card-header-title h5::text').extract()
        
        regex = re.compile(r'[\n\r\t]')
        # TO REMOVE UNWANTED SYMBOLS AND DATA
        for i in range(len(title)):
             title[i] = regex.sub("", title[i]) 
        # To remove empty string ('') from lists 
        while('' in title):
            title.remove('')

        for i in range(len(price)):
             price[i] = regex.sub("", price[i])

        for i in range(len(area)):
            area[i] = regex.sub("", area[i])

        for i in range(len(owner)):
            owner[i] = regex.sub("", owner[i])
        

        df1 = pd.DataFrame() 
        
        # items['images'] = images[::2]
        items['title'] = title
        items['price'] = price[::2]
        items['area'] = area
        items['owner'] = owner
        # items['furnishing'] = furnishing
        items['posted_date'] = posted_date[::2]

        yield items

        df = pd.DataFrame() 
        df = pd.DataFrame.from_dict(items, orient='index')
        df = df.transpose()	
        df.to_excel('07-09-2020_DewasNaka.xlsx')
		
        pass