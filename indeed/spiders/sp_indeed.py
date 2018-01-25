# -*- coding: utf-8 -*-
import scrapy


class SpIndeedSpider(scrapy.Spider):
    name = 'sp_indeed'
    allowed_domains = ['indeed.com']
    start_urls = ['https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=%E5%96%B6%E6%A5%AD&l=%E6%9D%B1%E4%BA%AC%E9%83%BD']

    def parse(self, response):
        for caset in response.css('div.result'):
            if(caset.css('.company a')):
                comp_name = caset.css('.company a::text').re_first('\n\s*(.*)')
            else:
                comp_name = caset.css('.company::text').re_first('\n\s*(.*)')
            yield {
                'comp_name': comp_name,
                'comp_link': caset.css('.company a::attr(href)').extract_first(),
                'review': caset.css('a span.slNoUnderline::text').re_first('([0-9]*)'),
            }
