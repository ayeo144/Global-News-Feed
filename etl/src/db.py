import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database


load_dotenv()

# Configure DB connection

user = os.getenv("AWS_DB_USERNAME")
pword = os.getenv("AWS_DB_PASSWORD")
host = os.getenv("AWS_DB_HOST")
port = os.getenv("AWS_DB_PORT")
db = os.getenv("AWS_DB_NAME")

DB_URL = DB_URL = f"postgresql://{user}:{pword}@{host}:{port}/{db}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()