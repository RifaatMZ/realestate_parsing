# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Compose
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags


def strip_string(values):
    return values.strip()


class UaeRealesateItem(scrapy.Item):
    _id = scrapy.Field()
    building = scrapy.Field(output_processor=TakeFirst())
    address = scrapy.Field(output_processor=TakeFirst())
    property_type = scrapy.Field(input_processor=MapCompose(strip_string), output_processor=TakeFirst())
    property_size = scrapy.Field(output_processor=TakeFirst())
    bedrooms = scrapy.Field(input_processor=MapCompose(strip_string), output_processor=TakeFirst())
    bathrooms = scrapy.Field(output_processor=TakeFirst())
    completion = scrapy.Field(input_processor=MapCompose(strip_string), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(strip_string), output_processor=TakeFirst())



