import scrapy
from ..items import NetflixSeriesDesc
from .series import SeriesSpider


class SeriesDesc(scrapy.Spider):
    name = 'description'
    urls = SeriesSpider.desc_url

    def parse_details(self, response):
        item = NetflixSeriesDesc()

        year = response.css('div.title-info-metadata-wrapper span::text').get()
        maturity_rating = response.css('div.title-info-metadata-wrapper span span span::text').get()
        no_of_seasons = response.css('span.test_dur_str::text').get()
        desc = response.css('div.title-info-synopsis::text').get()

        item['year'] = year
        item['maturity_rating'] = maturity_rating
        item['no_of_seasons'] = no_of_seasons
        item['desc'] = desc

        yield item
