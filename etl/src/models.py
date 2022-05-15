from sqlalchemy import Column, String, Integer, DateTime, Date, Float

from src.db import Base


class CountryLocations(Base):
    """
    Table to store spatial location of each country.
    """

    __tablename__ = "country_locations"

    id = Column(Integer, primary_key=True)
    country = Column(String)
    lon = Column(Float)
    lat = Column(Float)


class APIDataRequests(Base):
    """
    Table to store paths of directories containing the JSON file
    outputs of each request / set of requests made to the NewsAPI.
    """

    __tablename__ = "api_data_requests"

    id = Column(Integer, primary_key=True)
    path = Column(String)
    metadata_file = Column(String)


class RawAPIData(Base):
    """
    Table to store the records from JSON API responses.
    """

    __tablename__ = "raw_api_data"

    id = Column(Integer, primary_key=True)
    source = Column(String)
    author = Column(String)
    title = Column(String)
    url = Column(String)
    publish_date = Column(Date)
    country = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)


class Production(Base):
    """
    "Production-ready" data.
    """

    __tablename__ = "production"

    id = Column(Integer, primary_key=True)
    source = Column(String)
    author = Column(String)
    title = Column(String)
    url = Column(String)
    publish_date = Column(Date)
    country = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    lon = Column(Float)
    lat = Column(Float)
