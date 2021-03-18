import scrapy


class DataSpiderSpider(scrapy.Spider):
    name = 'data_spider'
    allowed_domains = ['https://www.hltv.org/results']
    start_urls = ['http://https://www.hltv.org/results/']

    def parse(self, response):
        pass
