#from sqlalchemy import Column, Integer, create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
from ..exts import db

# engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
# Session = sessionmaker(bind=engine)
# Base = declarative_base()

class Entity(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
