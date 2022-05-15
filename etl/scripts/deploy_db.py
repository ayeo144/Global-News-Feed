import sys
from pathlib import Path
from typing import List

import sqlalchemy_utils

SRC_DIR = Path(Path(__file__).parent.parent)
sys.path.insert(0, str(SRC_DIR))

from src.db import SessionLocal, engine
from src.models import Base, CountryLocations
from src.utils import read_config


COUNTRIES_COORDS_JSON = Path(SRC_DIR, "cfg", "un-country-centroids.json")
API_CFG = Path(SRC_DIR, "cfg", "news-api-cfg.yml")


def setup_db():
    """
    Create database, create tables, upload country coordinates
    to the "country_locations" table.
    """

    create_database(engine)
    print("Database create!")

    create_database_tables(engine)
    print("Tables created!")

    print("Uploading country coordinates...")
    upload_country_coordinates(SessionLocal)
    print("Upload completed!")


def create_database(engine):
    """
    Create database if it does exist.
    """

    if not sqlalchemy_utils.database_exists(engine.url):
        sqlalchemy_utils.create_database(engine.url)


def create_database_tables(engine):
    """
    Create all the tables in the database.
    """

    Base.metadata.create_all(bind=engine)


def upload_country_coordinates(db_session):
    """
    Upload the country coordinates to the database.
    """

    session = db_session()

    api_config = read_config(API_CFG)
    countries_coords = read_config(COUNTRIES_COORDS_JSON, loader="json")

    countries_coords_dict = _format_countries_json(countries_coords)
    available_countries = _map_countries(
        list(api_config["countries"].keys()), list(countries_coords_dict.keys())
    )

    for k, v in available_countries.items():

        lon = countries_coords_dict[v]["lon"]
        lat = countries_coords_dict[v]["lat"]

        record = CountryLocations(country=k, lon=lon, lat=lat)

        query = session.query(CountryLocations).filter_by(country=k).first()

        if query is None:
            session.add(record)

    session.commit()
    session.close()


def _format_countries_json(coords_list: List[dict]) -> dict:
    return {

        item["name"]: {

            "lon": item["long"], 
            "lat": item["lat"],

        } 

        for item in coords_list

    }


def _map_countries(
    countries_from_api: List[str], countries_with_coords: List[str]
) -> dict:
    mapping = {}

    for c in countries_from_api:
        if c not in mapping.keys():
            for c2 in countries_with_coords:
                if c.lower() in c2.lower():
                    mapping[c] = c2

    return mapping


def validate_db_setup():

    session = SessionLocal()
    query = session.query(CountryLocations).all()
    
    assert len(query) > 0, "db was not successfully created!"

    session.close()


if __name__ == '__main__':

    setup_db()
    validate_db_setup()