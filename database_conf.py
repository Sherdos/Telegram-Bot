from sqlalchemy import create_engine, Column, Integer, String


DB_NAME = 'telebot'
DB_PASS = '2007'
DB_PORT = '5432'
DB_USER = 'postgres'
DB_HOST = 'localhost'

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",echo=True)

