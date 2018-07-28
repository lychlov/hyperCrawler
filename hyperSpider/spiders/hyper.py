# -*- coding: utf-8 -*-
import scrapy


class HyperSpider(scrapy.Spider):
    name = 'hyper'
    allowed_domains = ['hypernum.com']
    start_urls = ['http://hypernum.com/']

    def parse(self, response):
        pass
