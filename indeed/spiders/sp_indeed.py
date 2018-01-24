# -*- coding: utf-8 -*-
import scrapy


class SpIndeedSpider(scrapy.Spider):
    name = 'sp_indeed'
    allowed_domains = ['indeed.com']
    start_urls = ['http://indeed.com/']

    def parse(self, response):
        pass
