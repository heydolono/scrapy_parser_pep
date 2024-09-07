import scrapy

from pep_parse.items import PepParseItem
from pep_parse.constants import (
    NAME_SPIDER,
    ALLOWED_DOMAINS,
    START_URLS,
)


class PepSpider(scrapy.Spider):
    name = NAME_SPIDER
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        for pep in response.css('section#numerical-index tbody tr'):
            number = pep.css('td:nth-child(2) a::text').get()
            name = pep.css('td:nth-child(3) a::text').get()
            status = pep.css('td:nth-child(1) abbr::attr(title)').get().strip()

            yield PepParseItem(number=number, name=name, status=status)

    def parse_pep(self, response):
        pass
