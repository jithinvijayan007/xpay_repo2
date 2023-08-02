


from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

engine = create_engine('postgresql://postgres:1234@localhost/xpay_db',
                       echo = True
                       )

Base = declarative_base()

Session = sessionmaker()

