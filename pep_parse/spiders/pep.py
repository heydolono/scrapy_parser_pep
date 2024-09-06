import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep in response.css('section#numerical-index tbody tr'):
            number = pep.css('td:nth-child(2) a::text').get()
            name = pep.css('td:nth-child(3) a::text').get()
            status = pep.css('td:nth-child(1) abbr::attr(title)').get().strip()

            yield PepParseItem(number=number, name=name, status=status)

    def parse_pep(self, response):
        pass
