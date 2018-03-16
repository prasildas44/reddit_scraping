import random
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from reddit.items import PicItem

class PicSpider(CrawlSpider):
    name = "pic"
    allowed_domains = ["www.reddit.com"]
    start_urls = ['http://www.reddit.com/r/weed/']

       

    rules = [
        Rule(LinkExtractor(
            allow=['/r/weed/\?count=\d*&after=\w*']),
        # '/r/pics/\?count=\d*&after=\w*'
            callback='parse_start_url',
            follow=True)
    ]

    # rules = [
    #     # Traverse the in the /r/pics subreddit. When you don't pass
    #     # callback then follow=True by default.
    #     # It's also important to NOT override the parse method
    #     # the parse method is used by the CrawlSpider continuously extract links
    #     Rule(LinkExtractor(
    #     	allow=['/r/pics/\?count=\d*&after=\w*']),
    #     	callback='parse_item',
    #     	follow=True),
    # ]

    def parse_start_url(self, response):
        
        

        
        item = PicItem()
        # item['image_urls'] = selector.xpath('a/@href').extract()
        item['title'] = response.xpath("//a[contains(@class, 'title may-blank')]/text()").extract()

        # item['url'] = selector.xpath('a/@href').extract()

            
        yield item

