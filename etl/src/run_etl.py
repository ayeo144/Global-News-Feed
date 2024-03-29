import os
import datetime
from pathlib import Path

from src.extract import Extractor
from src.load import Loader
from src.transform import create_production_table
from src.db import SessionLocal
from src.utils import read_config, S3Utils
from src.models import APIDataRequests
from src.config import Env


ETL_CFG = Path(Path(__file__).parent.parent, "cfg", "etl-cfg.yml")


def run_extract():
    """
    Run the raw data extraction process.

        1. Query API and get JSON response.
        2. Save JSON responses to files.
        3. Add the file paths to a database table to keep track of what requests have been made.
    """

    config = read_config(ETL_CFG)
    countries = config["query"]["countries"]

    # Extract data
    extract = Extractor(countries)
    extract.query()

    # Persist data
    root_dir = config["raw-storage"]["root-dir"]

    tstamp = datetime.datetime.now().strftime("%Y%md%d_%H%M%S")
    dirpath = os.path.join(root_dir, f"Responses_{tstamp}")

    metadata_file = extract.persist_to_s3(dirpath)

    _add_raw_data_record(dirpath, metadata_file)


def _add_raw_data_record(path, metadata_file):
    """
    Add the filepath of the new collection of responses to the database table.
    """

    session = SessionLocal()

    try:

        new_record = APIDataRequests(
            **{"path": str(path), "metadata_file": str(metadata_file)}
        )
        session.add(new_record)

        session.commit()

    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def run_load():
    """ 
    Take the data extracted from the API and saved as JSON files, and upload
    the records to a database table.
    """

    metadata_file = _get_last_metadata_file()
    metadata = S3Utils.json_to_dict(Env.S3_BUCKET_NAME, metadata_file)

    loader = Loader(metadata)
    loader.upload()


def _get_last_metadata_file() -> str:
    """
    Get the last metadata.json file created containing filepaths
    of the API responses for each different country from the latest
    data extraction.
    """
    
    session = SessionLocal()

    try:

        record = session.query(APIDataRequests).order_by(APIDataRequests.id.desc()).first()
        metadata_file = record.metadata_file

    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

    return metadata_file


def run_transform():
    """
    Take the latest API responses in the database and create the
    "production" tabl which can be readily consumed by the application.
    """

    create_production_table()
