from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from FocusEngine.items import FocusItem

from scrapy.spider import BaseSpider

class FocusSpider(CrawlSpider):
    name = "Focus"
    allowed_domains = ["sisciatech.tumblr.com",]
    start_urls = [
        "http://sisciatech.tumblr.com/post/37335459158/login-with-twitter-clojure-java-this-is-a-little"
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow=()), follow=True, callback='parse_item'),
         )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
       # print hxs.select('//title/text()').extract()
        item = FocusItem()
        item["text"] = hxs.select('//p/text()').extract()
        item["title"] = hxs.select('//title/text()').extract()
        return item