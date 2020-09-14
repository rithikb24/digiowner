import scrapy

class NBSpider(scrapy.Spider):
    name = 'nb_spider'
    start_urls = [
        'https://www.nobroker.in/property/rent/mumbai/Navi%20Mumbai/?searchParam=W3sibGF0IjoxOS4wMzMwNDg4LCJsb24iOjczLjAyOTY2MjUsInBsYWNlSWQiOiJDaElKclJNZnVQQzU1enNSYWZpRkVXajNFanciLCJwbGFjZU5hbWUiOiJOYXZpIE11bWJhaSJ9XQ==&sharedAccomodation=0&orderBy=nbRank,desc&radius=2&traffic=true&travelTime=30&propertyType=rent&pageNo=10'
    ]

    def parse(self, response):
        area = response.css('.solid-border-right meta+ span::text').extract()
        price = response.css('.solid-border-right .inr_resale+ span::text').extract()
        title = response.css('h2::text').extract()
        # owner_name = response.css('.seller-name span::text').extract()
        address = response.css('.card-header-title h5::text').extract()