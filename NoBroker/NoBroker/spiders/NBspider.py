import scrapy

class NBSpider(scrapy.Spider):
    name = 'nb_spider'
    start_urls = [
        'https://www.nobroker.in/property/rent/mumbai/Navi%20Mumbai/?searchParam=W3sibGF0IjoxOS4wMzMwNDg4LCJsb24iOjczLjAyOTY2MjUsInBsYWNlSWQiOiJDaElKclJNZnVQQzU1enNSYWZpRkVXajNFanciLCJwbGFjZU5hbWUiOiJOYXZpIE11bWJhaSJ9XQ==&sharedAccomodation=0&orderBy=nbRank,desc&radius=2&traffic=true&travelTime=30&propertyType=rent&pageNo=10'
    ]

    def parse(self, response):
        