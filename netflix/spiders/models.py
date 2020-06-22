from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Sequence, Float, create_engine , ForeignKey
from sqlalchemy.orm import relationship

import sqlite3

conn = sqlite3.connect('netflix.db')

engine = create_engine('sqlite:///netflix.db', echo=True)

Base = declarative_base()

class Series(Base):
    __tablename__ = "series"

    series_id = Column(Integer, Sequence('Series_id', minvalue=1000, increment=1), primary_key=True)
    series_name = Column(String)
    series_genre = Column(String)
    series_url = Column(String)
    series_img = Column(String)
    desc_id = relationship("SeriesDesc")


class SeriesDesc(Base):
    __tablename__ = "series_description"
    series_id = Column(Integer , ForeignKey('series.series_id'))
    desc_id = Column(Integer, Sequence('series_desc', minvalue=1000, increment=1), primary_key=True)
    year = Column(Integer)
    maturity_rating = Column(Float)
    no_of_seasons = Column(Integer)
    desc = Column(String)


Base.metadata.create_all(engine)
