import scrapy
from uae_realesate.items import UaeRealesateItem
from scrapy.loader import ItemLoader


class PropertyfinderSpider(scrapy.Spider):
    name = 'propertyfinder'
    allowed_domains = ['propertyfinder.ae']
    start_urls = ['http://propertyfinder.ae/en/buy/properties-for-sale.html']

    css_sel = {
        'pagination': 'div.pagination__links a::attr("href")',
        'post_urls': 'div.card-list__item a::attr("href")'
    }

    post_template = {
        'building': '//div[contains(@class, "property-location__detail-area")]/div[1]/text()',
        'address': '//div[contains(@class, "property-location__detail-area")]/div[last()]/text()',
        'property_type': '//div[contains(@class, "property-facts__column")][1]/div[contains(@class, "property-facts__list")][1]/div[2]/text()',
        'property_size': '//div[contains(@class, "property-facts__column")][1]/div[contains(@class, "property-facts__list")][2]//span[2]/text()',
        'bedrooms': '//div[contains(@class, "property-facts__column")][2]/div[contains(@class, "property-facts__list")][1]/div[2]/text()',
        'bathrooms': '//div[contains(@class, "property-facts__column")][2]/div[contains(@class, "property-facts__list")][2]/div[2]/text()',
        'completion': '//div[contains(@class, "property-facts__column")][1]/div[contains(@class, "property-facts__list")][3]/div[2]/text()',
        'price': '//div[contains(@class, "property-price")]/text()'
    }

    def parse(self, response):
        for url in response.css(self.css_sel['pagination']):
            yield response.follow(url, callback=self.parse)

        for post_url in response.css(self.css_sel['post_urls']):
            yield response.follow(post_url, callback=self.item_parse)

    def item_parse(self, response):

        item = ItemLoader(UaeRealesateItem(), response)

        item.add_xpath('building', self.post_template['building'])
        item.add_xpath('address', self.post_template['address'])
        item.add_xpath('property_type', self.post_template['property_type'])
        item.add_xpath('property_size', self.post_template['property_size'])
        item.add_xpath('bedrooms', self.post_template['bedrooms'])
        item.add_xpath('bathrooms', self.post_template['bathrooms'])
        item.add_xpath('completion', self.post_template['completion'])
        item.add_xpath('price', self.post_template['price'])

        yield item.load_item()
