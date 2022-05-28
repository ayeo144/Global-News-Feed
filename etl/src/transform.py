from src.db import engine
from src.models import RawAPIData, Production, CountryLocations


PROD_TABLE = "production"
RAW_TABLE = RawAPIData.__tablename__
COUNTRY_TABLE = CountryLocations.__tablename__


def create_production_table():
    """
    Creates the most up-to-date version of the "production"
    table.

    When you data is extracted from the API, cleaned and loaded
    into the database, this step is called to create an updated
    version of the "production" table.
    """
    
    _drop_table()
    _create_table()


def _drop_table():
    """
    If the "production" table exists, drop it.
    """

    query = f"DROP TABLE IF EXISTS {Production.name}"

    try:
        engine.execute(query)
    except Exception as e:
        raise e


def _create_table():
    """
    Create the "production" table. The "production" table will be used
    by the web application to serve the latest news headlines per country.

    Records with the latest timestamp are selected from the "raw_api_data"
    table and joined with longitude/latitude data for their particular
    country from the "country_locations" table to crrate the "production"
    table.
    """

    query = (
        f"""
        CREATE TABLE {PROD_TABLE} AS
        
        (
            SELECT raw_tbl.*, country_tbl.lon, country_tbl.lat FROM 

            (

                SELECT * FROM {RAW_TABLE}
                WHERE timestamp = (SELECT MAX(timestamp) FROM {RAW_TABLE})

            ) AS raw_tbl

            JOIN {COUNTRY_TABLE} AS country_tbl

            ON raw_tbl.country = country_tbl.country
        );
        """
    )

    try:
        engine.execute(query)
    except Exception as e:
        raise e
