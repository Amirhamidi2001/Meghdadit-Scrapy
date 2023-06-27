# from pathlib import Path
# import scrapy


# class MeghdaditSpider(scrapy.Spider):
#     name = "meghdadit"
#     start_urls = ["https://meghdadit.com/product/9/asus-vs197de-led-monitor/"]

#     def parse(self, response):
#         filename = f'product.html'
#         Path(filename).write_bytes(response.body)
#         self.log(f'Saved file {filename}')


import scrapy
from meghdadit.items import MeghdaditItem
from urllib.parse import urlparse, urlunparse
import re


# class MeghdaditSpider(scrapy.Spider):
#     name = "meghdadit"
#     allowed_domains = ["meghdadit.com"]
#     start_urls = ["https://meghdadit.com/"]

#     def parse(self, response):
#         # extract category URLs
#         category_urls = response.xpath('//ul[@class="second-level-ul"]/li//@href').extract()
#         for category_url in category_urls:
#             category_url = category_url.strip()
#             # check if the URL scheme is missing
#             parsed_url = urlparse(category_url)
#             if not parsed_url.scheme:
#                 # add the scheme to the URL
#                 category_url = urlunparse(("https", "meghdadit.com", parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
#             # follow category URL to extract product detail URLs
#             yield scrapy.Request(category_url, callback=self.parse_category)

#     def parse_category(self, response):
#         # extract product detail URLs
#         parse_pages = response.xpath('//a[@id="SharedMessage_ContentPlaceHolder1_rptList_hlkThumbnail_0"]/@href').extract()
#         for parse_page in parse_pages:
#             parse_page = parse_page.strip()
#             # check if the URL scheme is missing
#             parsed_url = urlparse(parse_page)
#             if not parsed_url.scheme:
#                 # add the scheme to the URL
#                 parse_page = urlunparse(("https", "meghdadit.com", parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
#             # follow product detail URL to extract title
#             yield scrapy.Request(parse_page, callback=self.parse_page)

#         # extract the URL of the next page if available
#         next_page = response.css('a#SharedMessage_ContentPlaceHolder1_hlkNextPage::attr(href)').get()
#         if next_page:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse_category)

#     def parse_page(self, response):
#         # Extract data from the response using XPath or CSS selectors
#         title = response.css("title::text").get()
#         # price = response.xpath('//span[@id="SharedMessage_ContentPlaceHolder1_rptRelevantProduct_lblGheymat_0"]/text()').get()
#         price = response.xpath("//div[@class='col col-xl-7 product-item-description']//span[@id='lblOriginalPrice']").get()
#         product_exist = True
#         product_id = re.search(r"/(\d+)/", response.url).group(1)
#         categories = response.css("a.bread-link::text").getall()

#         # Create a new item with the extracted data
#         item = MeghdaditItem()
#         item["title"] = title.strip()
#         item["price"] = price
#         item["url"] = response.url
#         item["product_exist"] = product_exist
#         item["product_id"] = product_id
#         item["domain"] = "meghdadit.com"
#         item["categories"] = [category.strip() for category in categories][:-1]

#         yield item


class MeghdaditSpider(scrapy.Spider):
    name = "meghdadit"
    allowed_domains = ["meghdadit.com"]
    start_urls = ["https://meghdadit.com/product/119611/sapphire-graphic-card-model-toxic-radeon-rx-6900-xt-extreme-edition-16gb/"]

    def parse(self, response):
        # Extract data from the response using XPath or CSS selectors
        title = response.css("title::text").get()
        url = response.url
        price = response.xpath("//input[@id='hfdPrices']/@value").get()
        if price is not None:
            price = price.strip()
            product_exist = True
        else:
            price = None
            product_exist = False
        product_id = re.search(r"/(\d+)/", response.url).group(1)
        categories = response.css("a.bread-link::text").getall()

        # Create a new item with the extracted data
        item = MeghdaditItem()
        item["title"] = title.strip()
        # item["price"] = price
        item["product_exist"] = product_exist
        item["product_id"] = product_id
        item["url"] = url
        item["domain"] = "meghdadit.com"
        item["categories"] = [category.strip() for category in categories][:-1]
        item["currency"] = "تومان"

        yield item

# import scrapy

# class MonitorSpider(scrapy.Spider):
#     name = 'monitor'
#     start_urls = ['https://meghdadit.com/product/9/asus-vs197de-led-monitor/']

#     def parse(self, response):
#         price_xpath = '//input[@id="hfdPrices"]/@value'
#         price = response.xpath(price_xpath).get()

#         yield {"price":price}
