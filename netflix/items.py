# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy


class NetflixItem(scrapy.Item):
    series_name = scrapy.Field()
    series_genre = scrapy.Field()
    series_url = scrapy.Field()
    series_img = scrapy.Field()

