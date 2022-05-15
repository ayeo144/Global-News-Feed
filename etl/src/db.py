from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database

from src.config import Env

# Configure DB connection

user = Env.DB_USERNAME
pword = Env.DB_PASSWORD
host = Env.DB_HOST
port = Env.DB_PORT
db = Env.DB_NAME

DB_URL = f"postgresql://{user}:{pword}@{host}:{port}/{db}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
