from sqlalchemy import Column, String, Integer, DateTime

from src.db import Base


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

    id = Column(Integer, primary_key)
    source = Column(String)
    author = Column(String)
    title = Column(String)
    url = Column(String)
    publish_date = Column(DateTime)
    country = Column(String, required=True)
