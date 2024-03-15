from sqlalchemy import Column, Integer, String
from database_conf import engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    
    def __str__(self):
        return f'{self.title}'
    
class Sentens(Base):
    __tablename__ = 'sentens'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    
    def __str__(self):
        return f'{self.title}'

Base.metadata.create_all(engine)