import sqlite3

conn = sqlite3.connect('netflix.db')
curr = conn.cursor()

curr.execute("""create table series_tb(
             series_name text,
             series_genre text,
             series_url text,
             series_img text
             )""")

curr.execute("""insert into series_tb values""")

conn.commit()
conn.close()
