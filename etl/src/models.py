from sqlalchemy import Column, String, Integer

from src.db import Base


class APIDataRequests(Base):
    """
    Table to store paths of directories containing the JSON file
    outputs of each request / set of requests made to the NewsAPI.
    """

    __tablename__ = "api_data_requests"

    id = Column(Integer, primary_key=True)
    path = Column(String)