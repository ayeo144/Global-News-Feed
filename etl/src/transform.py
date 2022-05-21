from src.db import engine
from src.models import RawAPIData, Production, CountryLocations


class Queries:

    DROP_TABLE = f"DROP TABLE IF EXISTS {Production.name}"

    CREATE_TABLE_AS = f"CREATE TABLE {Production.name} AS"

    SELECT_LATEST_RAW = (
        f"""
        SELECT * FROM {RawAPIData.__tablename__}
        WHERE timestamp = (SELECT MAX(timestamp) FROM {RawAPIData.__tablename__})
        """
    )


def _drop_table():

    try:
        engine.execute(f"{Queries.DROP_TABLE};")
    except Exception as e:
        raise e

def _create_table():

    try:
        engine.execute(
            f"""
            {Queries.CREATE_TABLE_AS}
            (
                SELECT raw_tbl.*, country_tbl.lon, country_tbl.lat FROM 

                ({Queries.SELECT_LATEST_RAW}) AS raw_tbl

                JOIN {CountryLocations.__tablename__} AS country_tbl

                ON raw_tbl.country = country_tbl.country
            );
            """
        )
    except Exception as e:
        raise e
