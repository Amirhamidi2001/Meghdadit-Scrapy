# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeghdaditItem(scrapy.Item):
    title = scrapy.Field()
    # price = scrapy.Field()
    url = scrapy.Field()
    product_exist = scrapy.Field()
    product_id = scrapy.Field()
    domain = scrapy.Field()
    categories = scrapy.Field()
    currency = scrapy.Field()
