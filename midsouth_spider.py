import scrapy
from ..items import MidsouthsshooterItem

class midsouthSpider(scrapy.Spider):
    name = 'midsouth'
    start_urls = [
        'https://www.midsouthshooterssupply.com/dept/reloading/primers'
    ]

    def parse(self, response):

        items=MidsouthsshooterItem()

        title=response.css(".page-title::text").extract()
        price=response.css(".price span::text").extract()
        status = response.css(".out-of-stock::text").extract()
        manufacturer = response.css(".catalog-item-brand::text").extract()
        description=response.css(".catalog-item-name::text").extract()
        #riview = response.css(".pr-rd-review-headline::text").extract()

        items['title']=title
        items['price']=price
        items['status']=status
        items['manufacturer']=manufacturer
        items['description']=description
        #items['review']=review

        yield items