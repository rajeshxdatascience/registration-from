from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv('DB_PASSWORD')

connection_url = URL.create("postgresql+psycopg2", username="postgres", password=PASSWORD, host="localhost", port=5432, database="registration_db")

engine = create_engine(connection_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()