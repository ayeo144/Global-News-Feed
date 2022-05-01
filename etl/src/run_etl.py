import os
import datetime
from pathlib import Path

from src.extract import Extractor
from src.utils import read_config
from src.db import engine, SessionLocal
from src.models import Base, APIDataRequests


ETL_CFG = Path(Path(__file__).parent.parent, "cfg", "etl-cfg.yml")

Base.metadata.create_all(bind=engine)


def run_extract():
    """
    Run the ETL process.

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
    storage_type = config["raw-storage"]["type"]
    root_dir = config["raw-storage"]["root-dir"]

    tstamp = datetime.datetime.now().strftime("%Y%md%d_%H%M%S")
    dirpath = os.path.join(root_dir, f"Responses_{tstamp}")

    metadata = extract.persist(dirpath, storage=config["raw-storage"]["type"])

    _add_raw_data_record(dirpath)

    return metadata


def _add_raw_data_record(path):
    """
    Add the filepath of the new collection of responses to the database table.
    """

    session = SessionLocal()

    new_record = APIDataRequests(**{"path": str(path)})
    session.add(new_record)

    session.commit()
    session.close()
