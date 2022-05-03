import os
import json
import datetime
from typing import Optional, List, Dict

import pandas as pd
from pydantic import BaseModel
from dotenv import load_dotenv

from src.db import engine
from src.utils import S3Utils
from src.models import RawAPIData


load_dotenv()


class Article(BaseModel):
    """
    Data validation layer.
    """

    source: Optional[str] = None
    author: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    publish_date: Optional[datetime.datetime] = None
    country: str
    date: datetime.date


class Loader:
    """
    Load data from the extraction phase into the database.

    Data needs to be taken from the JSON files, useful content extracted
    and then loaded into a database table.

    Take metadata file created during Extract phase, read json files, add to db.
    """

    S3_BUCKET = os.getenv("S3_BUCKET_NAME")

    def __init__(self, metadata: Dict[str, list]):
        self.metadata = metadata

    def upload(self):

        for country, json_file in self.metadata.items():

            json_data = S3Utils.json_to_dict(Loader.S3_BUCKET, json_file)
            articles_df = Loader.prepare_country_articles(json_data["articles"], country)
            Loader.records_to_sql(articles_df)

    @classmethod
    def prepare_country_articles(cls, articles: List[dict], country: str) -> pd.DataFrame:
        """
        Take a list of news articles stored in dictionaries and prepare them
        for upload to the database.
        """

        articles_list = [cls.prepare_article(article, country).dict() for article in articles]
        articles_df = pd.DataFrame(records_list)
        articles_df = articles_df.drop_duplicates()

        return articles_df

    @staticmethod
    def prepare_article(article: dict, country: str) -> Article:
        return Article(
            source=article["source"]["name"],
            author=article["author"],
            title=article["title"],
            url=article["url"],
            publish_date=datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"),
            country=country,
            date=datetime.date.today(),
        )

    @staticmethod
    def records_to_sql(df: pd.DataFrame):
        df.to_sql(RawAPIData.__tablename__, engine, if_exists="append")
