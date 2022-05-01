import os
import json
import argparse
from pathlib import Path
from typing import Union, List

import yaml
import boto3
from dotenv import load_dotenv
from newsapi import NewsApiClient


load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
API_CFG = Path(Path(__file__).parent.parent, 'cfg', 'news-api-cfg.yml')


class Extract:
    """
    Class to handle extracting data from the NewsAPI for different countries.
    """

    def __init__(self, country: Union[str, List[str]]):
        if isinstance(country, str):
            country = [country]
        self.country_list = country

    def query(self, debug: bool = False):
        """
        Query the API to get responses for all countries.
        """

        self.responses = {}

        for country in self.country_list:

            articles = Extract.get_all_headlines(country)
            self.responses[country] = articles

            if debug:
                print(f"Found {len(articles)} for {country}")

    def persist(self, dirpath: str, storage: str = "s3"):
        """
        Persist API JSON responses to JSON files in a storage location.
        """

        for country in self.country_list:

            fname = f"{country}.json"

            if storage == "s3":

                dirpath = dirpath.replace("\\", "/")
                fpath = dirpath + "/" + fname
                Extract.save_articles_json_to_s3(self.responses[country], fpath)

            if storage == "local":

                dirpath = Path(dirpath)

                if not dirpath.is_dir():
                    raise Exception("Directory does not exist!")

                fpath = Path(dirpath, fname)

                Extract.save_articles_json_to_local(self.responses[country], fpath)

    @classmethod
    def get_all_headlines(cls, country: str) -> List[dict]:
        """
        Get all possible top headlines for a country, with duplicated responses removed.
        """

        response_1 = cls.query_all_top_headlines_by_country(country)
        response_2 = cls.get_top_headlines_for_country(country)
        response_3 = cls.query_bbc_top_headlines_by_country(country)

        articles = response_1["articles"] + response_2["articles"] + response_3["articles"]

        return cls._remove_duplicate_articles(articles)

    @staticmethod
    def query_bbc_top_headlines_by_country(country: str, language: str = "en", page: int = 1) -> dict:
        """
        Query the top BBC News headlines using the country name as a keyword.
        """

        api = NewsApiClient(api_key=API_KEY)
        return api.get_top_headlines(q=country, sources="bbc-news", language=language, page=page)

    @staticmethod
    def query_all_top_headlines_by_country(country: str, language: str = "en", page: int = 1) -> dict:
        """
        Query all top headlines using the country name a keyword for the query.
        """

        api = NewsApiClient(api_key=API_KEY)
        return api.get_top_headlines(q=country, language=language, page=page)

    @classmethod
    def get_top_headlines_for_country(cls, country: str, language: str = "en", page: int = 1) -> dict:
        """
        Get the top headlines for a country from the API for specific country-code.
        """

        api = NewsApiClient(api_key=API_KEY)
        country = cls.get_country_iso_code(country)
        return api.get_top_headlines(country=country, language=language, page=page)

    @classmethod
    def get_country_iso_code(cls, country: str):
        """
        Get the ISO 3166-1 code for the country from the configuration file.
        """
        config = cls._read_cfg(API_CFG)
        return config["countries"][country].lower()

    @staticmethod
    def _read_cfg(file: Union[Path, str]) -> dict:
        with open(file) as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    @classmethod
    def _remove_duplicate_articles(cls, articles: List[dict]) -> List[dict]:
        """
        Remove duplicate articles from a list of articles represented
        as dicts from the API response, using the website URL to identify
        duplicates.

        Returns the list of unique articles.
        """

        unique_urls_dict = {a['url']: i for i, a in enumerate(articles)}
        all_urls_list = [a['url'] for a in articles]

        removed_urls = []

        for dupe_url in cls._find_duplicates(all_urls_list):
            
            if dupe_url not in removed_urls:
                
                index = unique_urls_dict[dupe_url]
                articles.pop(index)
                removed_urls.append(dupe_url)
                
        return articles

    @staticmethod
    def _find_duplicates(lst: list) -> list:
        return list(set([x for x in lst if lst.count(x) > 1]))

    @staticmethod
    def save_articles_json_to_s3(articles: List[dict], fpath: str):
        """
        Save the list of articles from the API to JSON in an S3 bucket.
        """

        aws_session = boto3.Session(
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        )
        s3 = aws_session.client('s3')

        bucket_name = os.getenv("S3_BUCKET_NAME")

        s3_put_response = s3.put_object(
            Body=json.dumps({"articles": articles}, ensure_ascii=False), 
            Bucket=bucket_name,
            Key=fpath,
        )

        status_code = s3_put_response["ResponseMetadata"]["HTTPStatusCode"] 
        if status_code != 200:
            raise Exception(f"S3 PUT status code = {status_code}!")

    @staticmethod
    def save_articles_json_to_local(articles: List[dict], fpath: str):
        """
        Save the list of articles from the API to JSON on local storage.
        """

        with open(fpath, "wb") as f:
            json.dumps({"articles": articles}, f)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--country", "-c", type=str, required=True)
    parser.add_argument("--path", "-p", type=str, required=False)

    options = parser.parse_args()

    extract = Extract(options.country)
    extract.query()

    if options.path:

        extract.persist(path)

    print(response)
