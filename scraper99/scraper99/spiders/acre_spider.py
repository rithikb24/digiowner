
import scrapy
from ..items import Scraper99Item
import pandas as pd

class AcreSpiderSpider(scrapy.Spider):
	name = 'acre_spider'
	start_urls = ['https://www.99acres.com/rent-property-in-bhanvarkuan-indore-ffid?src=CLUSTER']

	def parse(self, response):

		items = Scraper99Item()

		#price = response.xpath("//div[@id='priceProperty47557783']//text").extract()
		#area = response.xpath("//div[contains(text(),'830 sqft')]//text").extract()
		
		title = response.css('h2').css('::text').extract()
		price = response.css('#srp_tuple_price::text').extract()
		area = response.css('#srp_tuple_primary_area::text').extract()
		bhk = response.css('#srp_tuple_bedroom::text').extract()
		# owner_name = response.css('.list_header_semiBold a::text').extract()
		date_of_posting = response.css('.caption_strong_small span::text').extract()

		items['title'] = title
		items['price'] = price
		items['area'] = area
		items['bhk'] = bhk
		# items['owner_name'] = owner_name
		items['date_of_posting'] = date_of_posting

		#yield items


		#for item in zip(title, price, area, bhk, owner_name, date_of_posting):

		scraped_info = {
		'title' : title,
		'price' : price,
		'area' : area,
		'bhk' : bhk,
		# 'owner_name' : owner_name,
		'date_of_posting' : date_of_posting,
		}

		df = pd.DataFrame.from_dict(scraped_info, orient='index')
		df = df.transpose()	
		# df.head()
		df.to_excel("bhavarkuan.xlsx")
		yield scraped_info

		



		
		
