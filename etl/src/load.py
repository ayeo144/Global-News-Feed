import datetime
from typing import Optional, List, Dict

import pandas as pd
from pydantic import BaseModel

from src.db import engine
from src.utils import S3Utils
from src.models import RawAPIData
from src.config import Env


class Article(BaseModel):
    """
    Data validation layer.
    """

    source: Optional[str] = None
    author: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    publish_date: Optional[datetime.date] = None
    country: str
    timestamp: datetime.datetime


class Loader:
    """
    Load data from the extraction phase into the database.

    Data needs to be taken from the JSON files, useful content extracted
    and then loaded into a database table.

    Take metadata file created during Extract phase, read json files, add to db.
    """

    S3_BUCKET = Env.S3_BUCKET_NAME

    def __init__(self, metadata: Dict[str, list]):
        self.metadata = metadata

    def upload(self):

        timestamp = datetime.datetime.utcnow()

        for country, json_file in self.metadata.items():

            json_data = S3Utils.json_to_dict(Loader.S3_BUCKET, json_file)
            articles_df = Loader.prepare_country_articles(
                json_data["articles"], country, timestamp
            )
            Loader.records_to_sql(articles_df)

    @classmethod
    def prepare_country_articles(
        cls, articles: List[dict], country: str, timestamp: datetime.datetime
    ) -> pd.DataFrame:
        """
        Take a list of news articles stored in dictionaries and prepare them
        for upload to the database.
        """

        articles_list = [
            cls.prepare_article(article, country, timestamp).dict() for article in articles
        ]
        articles_df = pd.DataFrame(articles_list)
        articles_df = articles_df.drop_duplicates()

        return articles_df

    @staticmethod
    def prepare_article(article: dict, country: str, timestamp: datetime.datetime) -> Article:
        return Article(
            source=article["source"]["name"],
            author=article["author"],
            title=article["title"],
            url=article["url"],
            publish_date=datetime.datetime.strptime(
                article["publishedAt"][0:10], "%Y-%m-%d"
            ),
            country=country,
            timestamp=timestamp,
        )

    @staticmethod
    def records_to_sql(df: pd.DataFrame):
        df.to_sql(RawAPIData.__tablename__, engine, if_exists="append", index=False)
