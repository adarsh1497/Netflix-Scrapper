# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3


class NetflixPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('netflix.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS series_tb""")
        self.curr.execute("""create table series_tb(
                            series_name text,
                            series_genre text,
                            series_url text,
                            series_img text
                            )""")

    def store_db(self, item):
        self.curr.execute("""insert into series_tb values(?,?,?,?) """, (
            item['series_name'],
            item['series_genre'],
            item['series_url'],
            item['series_img'],
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
