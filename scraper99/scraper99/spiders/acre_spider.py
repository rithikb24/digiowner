
import scrapy
from ..items import Scraper99Item
import pandas as pd

class AcreSpiderSpider(scrapy.Spider):
	name = 'acre_spider'
	page_number = 2
	start_urls = [
		'https://www.99acres.com/search/property/rent/vijay-nagar-indore?city=142&locality=9438&preference=R&area_unit=1&budget_min=0&res_com=R?page=1'
		]

	def parse(self, response):

		items = Scraper99Item()

		#price = response.xpath("//div[@id='priceProperty47557783']//text").extract()
		#area = response.xpath("//div[contains(text(),'830 sqft')]//text").extract()
		
		title = response.css('h2').css('::text').extract()
		price = response.css('#srp_tuple_price::text').extract()
		area = response.css('#srp_tuple_primary_area::text').extract()
		bhk = response.css('#srp_tuple_bedroom::text').extract()
		owner_name = response.css('.list_header_semiBold a::text').extract()
		date_of_posting = response.css('.caption_strong_small span::text').extract()
		link = response.xpath('//a[@class="body_med srpTuple__propertyName"]/@href').extract()

		items['title'] = title
		items['price'] = price
		items['area'] = area
		items['bhk'] = bhk
		items['owner_name'] = owner_name
		items['date_of_posting'] = date_of_posting
		items['link'] = link

		yield items

		next_page = 'https://www.99acres.com/search/property/rent/vijay-nagar-indore?city=142&locality=9438&preference=R&area_unit=1&budget_min=0&res_com=R?page='+str(AcreSpiderSpider.page_number)

		if AcreSpiderSpider.page_number <= 3:
			AcreSpiderSpider.page_number += 1
			yield response.follow(next_page, callback=self.parse)

		#for item in zip(title, price, area, bhk, owner_name, date_of_posting):

		# scraped_info = {
		# 'title' : title,
		# 'price' : price,
		# 'area' : area,
		# 'bhk' : bhk,
		# # 'owner_name' : owner_name,
		# 'date_of_posting' : date_of_posting,
		# }

		df = pd.DataFrame.from_dict(items, orient='index')
		df = df.transpose()	
		# df.head()
		df.to_excel("owner_name_vn.xlsx")
		# yield scraped_info



		



		
		
