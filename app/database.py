from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

import time
import psycopg2
from psycopg2.extras import RealDictCursor

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"



# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Zuzz%408021@localhost:5432/fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# 👇 Add this at the bottom of your database.py
from sqlalchemy.orm import Session
from typing import Generator

#dependency to get a database session withh annonation it endure the typesafety auto-completion on the returned object (e.g., if you mistype db.query()
# def get_db() -> Generator[Session, None, None]:
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#This is to make a creation with Postgressql

def get_db_connection():
    """Establish a PostgreSQL connection using psycopg2 with retry logic."""
    while True:
        try:
            conn = psycopg2.connect(
                host='localhost',
                database='fastapi',
                user='postgres',
                password='Zuzz@8021',
                cursor_factory=RealDictCursor
            )
            cursor = conn.cursor()
            print("✅ Connected to PostgreSQL using psycopg2")
            return conn, cursor
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            time.sleep(2)
            
# model.Base.metadata.create_all(bind=engine)