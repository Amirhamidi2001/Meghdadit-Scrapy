# Extraction of detail product information

# from pathlib import Path
# import scrapy


# class MeghdaditSpider(scrapy.Spider):
#     name = "meghdadit"

#     def start_requests(self):
#         urls = [
#             "https://meghdadit.com/product/41384/benq-gw2270h-va-led-eye-care-monitor/"
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         filename = f'monitor.html'
#         Path(filename).write_bytes(response.body)
#         self.log(f'Saved file {filename}')


# import scrapy
# from meghdadit.items import MeghdaditItem
# from urllib.parse import urlparse, urlunparse

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

#     def parse_page(self, response):
#         # Extract data from the response using XPath or CSS selectors
#         title = response.css("title::text").get()
#         price = response.xpath('//span[@id="SharedMessage_ContentPlaceHolder1_rptRelevantProduct_lblGheymat_0"]/text()').get()
#         product_exist = True
#         categories = response.css("a.bread-link::text").getall()

#         # Create a new item with the extracted data
#         item = MeghdaditItem()
#         item["title"] = title.strip()
#         item["price"] = price
#         item["url"] = response.url
#         item["product_exist"] = product_exist
#         item["domain"] = "meghdadit.com"
#         item["categories"] = [category.strip() for category in categories][:-1]

#         yield item


# import scrapy
# from meghdadit.items import MeghdaditItem
# from urllib.parse import urlparse, urlunparse


# class MeghdaditSpider(scrapy.Spider):
#     name = "meghdadit"
#     allowed_domains = ["meghdadit.com"]
#     start_urls = ["https://meghdadit.com/product/41384/benq-gw2270h-va-led-eye-care-monitor/"]

#     def parse(self, response):
#         # Extract data from the response using XPath or CSS selectors
#         title = response.css("title::text").get()
#         try:
#             price = response.xpath('//span[@id="SharedMessage_ContentPlaceHolder1_rptRelevantProduct_lblGheymat_0"]/text()').get()
#             product_exist = True
#         except:
#             price = None
#             product_exist = False
#         categories = response.css("a.bread-link::text").getall()

#         # Create a new item with the extracted data
#         item = MeghdaditItem()
#         item["title"] = title.strip()
#         item["price"] = price
#         item["url"] = response.url
#         item["product_exist"] = product_exist
#         item["domain"] = "meghdadit.com"
#         item["categories"] = [category.strip() for category in categories][:-1]

#         yield item




import scrapy
from meghdadit.items import MeghdaditItem
from urllib.parse import urlparse, urlunparse

class MeghdaditSpider(scrapy.Spider):
    name = "meghdadit"
    allowed_domains = ["meghdadit.com"]
    start_urls = ["https://meghdadit.com/"]

    def parse(self, response):
        # extract category URLs
        category_urls = response.xpath('//ul[@class="second-level-ul"]/li//@href').extract()
        for category_url in category_urls:
            category_url = category_url.strip()
            # check if the URL scheme is missing
            parsed_url = urlparse(category_url)
            if not parsed_url.scheme:
                # add the scheme to the URL
                category_url = urlunparse(("https", "meghdadit.com", parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
            # follow category URL to extract product detail URLs
            # yield scrapy.Request(category_url, callback=self.parse_category)
            yield {"category_url":category_url}
