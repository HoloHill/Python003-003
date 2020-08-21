# -*- coding: utf-8 -*-
import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MaoyanspiderSpider(scrapy.Spider):
    name = 'maoyanspider'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films']

    
    def start_requests(self):
        yield scrapy.Request(url=f'https://maoyan.com/films',callback=self.parse)

    def parse(self, response):
        tags = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')[:10]
        for tag in tags: 
            url = f'https://maoyan.com' + tag.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse2)
        
    def parse2(self, response):
        Selector(response=response).xpath
        item = MaoyanItem()

        # 电影名称
        movie_name = Selector(response=response).xpath('//h1[@class="name"]/text()').extract_first()

        # 电影类别
        all_list = Selector(response=response).xpath('//li[@class="ellipsis"][1]') # 所有类别的上级标签
        movie_cate_tags = all_list.xpath('./a[@class="text-link"]')# 所有的类别标签
        movie_cates = ''
        for movie_cate_tag in movie_cate_tags:
            movie_cate = movie_cate_tag.xpath('text()').extract_first().strip() # 取出类别内容
            movie_cates = movie_cates + movie_cate + '/'
        movie_cates = movie_cates[:-1]

        # 电影上映日期
        movie_release_date = Selector(response=response).xpath('//li[@class="ellipsis"][3]/text()').extract_first()[:10]
        
        # 储存到item
        item['movie_name'] = movie_name
        item['movie_cates'] = movie_cates
        item['movie_release_date'] = movie_release_date
        yield item
