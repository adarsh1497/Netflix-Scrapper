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


Base.metadata.create_all(engine)
