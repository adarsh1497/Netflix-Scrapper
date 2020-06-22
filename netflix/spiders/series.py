import scrapy
from ..items import NetflixItem

desc_url = []


class SeriesSpider(scrapy.Spider):
    name = "series"
    start_urls = [
        'https://www.netflix.com/in/browse/genre/83'
    ]

    def parse(self, response):
        item = NetflixItem()
        divs = response.css('div.nm-collections-container')

        for div in divs.xpath('.//div'):
            for section in div.xpath('.//section'):
                for web_series in section.xpath('.//div//ul//li//a'):
                    series_name = web_series.css('span.nm-collections-title-name::text').get()
                    series_genre = section.css('h1.nm-collections-row-name::text').get()
                    series_url = web_series.css('a::attr(href)').get()
                    series_img = web_series.xpath('.//img').css('img::attr(src)').get()
                    desc_url.append(series_url)
                    item['series_name'] = series_name
                    item['series_genre'] = series_genre
                    item['series_url'] = series_url
                    item['series_img'] = series_img

                    yield item

