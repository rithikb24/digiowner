
import scrapy
from ..items import Scraper99Item
import pandas as pd

class AcreSpiderSpider(scrapy.Spider):
	name = 'acre_spider'
	start_urls = ['https://www.99acres.com/search/property/buy/residential-all/south-tukoganj-indore?search_type=QS&refSection=GNB&search_location=NRI&lstAcn=NR_R&lstAcnId=-1&src=CLUSTER&preference=S&selected_tab=1&city=142&res_com=R&property_type=R&isvoicesearch=N&keyword_suggest=South%20Tukoganj%2C%20Indore%3B&class=O&fullSelectedSuggestions=South%20Tukoganj%2C%20Indore&strEntityMap=W3sidHlwZSI6ImxvY2FsaXR5In0seyIxIjpbIlNvdXRoIFR1a29nYW5qLCBJbmRvcmUiLCJDSVRZXzE0MiwgTE9DQUxJVFlfMjM1NTksIFBSRUZFUkVOQ0VfUywgUkVTQ09NX1IiXX1d&texttypedtillsuggestion=south%20tuko&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&suggestion=CITY_142%2C%20LOCALITY_23559%2C%20PREFERENCE_S%2C%20RESCOM_R&searchform=1&locality=23559&price_min=null&price_max=null']

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

		items['title'] = title
		items['price'] = price
		items['area'] = area
		items['bhk'] = bhk
		items['owner_name'] = owner_name
		items['date_of_posting'] = date_of_posting

		#yield items


		#for item in zip(title, price, area, bhk, owner_name, date_of_posting):

		scraped_info = {
		'title' : title,
		'price' : price,
		'area' : area,
		'bhk' : bhk,
		'owner_name' : owner_name,
		'date_of_posting' : date_of_posting,
		}

		df = pd.DataFrame.from_dict(scraped_info, orient='index')
		df.transpose()	
		df.head()
		df.to_excel("st.xlsx")
		yield scraped_info

		



		
		
