import os
import json
import argparse
from pathlib import Path
from typing import Union, List

import yaml
from dotenv import load_dotenv
from newsapi import NewsApiClient

from src.utils import S3Utils, read_config


load_dotenv()

API_CFG = Path(Path(__file__).parent.parent, "cfg", "news-api-cfg.yml")


class Extractor:
    """
    Class to handle extracting data from the NewsAPI for different countries.
    """

    API = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
    S3_BUCKET = os.getenv("S3_BUCKET_NAME")

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

            articles = Extractor.get_all_headlines(country)
            self.responses[country] = articles

            if debug:
                print(f"Found {len(articles)} for {country}")

    def persist_to_s3(self, dirpath: str) -> dict:
        """
        Persist API JSON responses to JSON files in a storage location. Save a 'metadata'
        JSON file containing the countries and filepaths of JSON requests which can be
        passed into the method for loading data from raw JSON dumps to the database.
        """

        metadata = {}
        dirpath = dirpath.replace("\\", "/")

        for country in self.country_list:

            fname = f"{country}.json"

            fpath = dirpath + "/" + fname
            articles = {"articles": self.responses[country]}
            S3Utils.dict_to_json(articles, Extractor.S3_BUCKET, fpath)

            metadata[country] = fpath

        metadata_file = dirpath + "/" + "METADATA.json"
        S3Utils.dict_to_json(metadata, Extractor.S3_BUCKET, metadata_file)

        return metadata_file

    @classmethod
    def get_all_headlines(cls, country: str) -> List[dict]:
        """
        Get all possible top headlines for a country, with duplicated responses removed.
        """

        response_1 = cls.query_all_top_headlines_by_country(country)
        response_2 = cls.get_top_headlines_for_country(country)
        response_3 = cls.query_bbc_top_headlines_by_country(country)

        articles = (
            response_1["articles"] + response_2["articles"] + response_3["articles"]
        )

        return articles

    @classmethod
    def query_bbc_top_headlines_by_country(
        cls, country: str, language: str = "en", page: int = 1
    ) -> dict:
        """
        Query the top BBC News headlines using the country name as a keyword.
        """

        return cls.API.get_top_headlines(
            q=country, sources="bbc-news", language=language, page=page
        )

    @classmethod
    def query_all_top_headlines_by_country(
        cls, country: str, language: str = "en", page: int = 1
    ) -> dict:
        """
        Query all top headlines using the country name a keyword for the query.
        """

        return cls.API.get_top_headlines(q=country, language=language, page=page)

    @classmethod
    def get_top_headlines_for_country(
        cls, country: str, language: str = "en", page: int = 1
    ) -> dict:
        """
        Get the top headlines for a country from the API for specific country-code.
        """

        country = cls.get_country_iso_code(country)
        return cls.API.get_top_headlines(country=country, language=language, page=page)

    @classmethod
    def get_country_iso_code(cls, country: str):
        """
        Get the ISO 3166-1 code for the country from the configuration file.
        """

        config = read_config(API_CFG)
        return config["countries"][country].lower()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--country", "-c", type=str, required=True)
    parser.add_argument("--path", "-p", type=str, required=False)

    options = parser.parse_args()

    extract = Extractor(options.country)
    extract.query(debug=True)

    if options.path:

        extract.persist_to_s3(path)

    print(extract.responses)
