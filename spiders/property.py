import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PropertySpider(CrawlSpider):
    name = "property"
    # allowed_domains = ["wwww.bdproperty.com"]
    start_urls = [
        "https://www.bproperty.com/en/dhaka/apartments-for-rent/"
        ]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//article[@class="ca2f5674"]/div/a'),
             callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[@title="Next"]'), follow=True),
        )

    def parse_item(self, response):

        yield {
            'title': response.xpath('//div[@aria-label="Property overview"]/h1/text()').get(),
            'price': response.xpath('//span[@class="_105b8a67"]/text()').get(),
            'location': response.xpath('//div[@aria-label="Property header"]/text()').get(),
            'beds': response.xpath('//span[@aria-label="Beds"]/span/text()').get(),
            'baths': response.xpath('//span[@aria-label="Baths"]/span/text()').get(),
            'area': response.xpath('//span[@aria-label="Area"]/span/span/text()').get(),
            'property_type': response.xpath('//span[@aria-label="Type"]/text()').get(),
            'property_id': response.xpath('//span[@aria-label="Reference"]/text()').get(),
            'last_update': response.xpath('//span[@aria-label="Updated date"]/text()').get()
        }
