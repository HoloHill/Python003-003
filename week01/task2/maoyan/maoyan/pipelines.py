# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_cates = item['movie_cates']
        movie_release_date = item['movie_release_date']
        
        # 把字段整合到一个字符串中
        output = f'|{movie_name}|\t|{movie_cates}|\t|{movie_release_date}|\n\n'

        with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
