from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

'''connect_url = URL(
    "oracle+cx_oracle",
    username="soumyakp",
    password="soumyakp",
    host="illin659",
    port="1521",
    database="Soumyakp",
)'''
engine = create_engine("oracle+cx_oracle://soumyakp:soumyakp@illin659:1521/?service_name=dmcnv")
#engine = create_engine(connect_url, max_identifier_length=128)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()