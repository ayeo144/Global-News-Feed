import os
import sys
from pathlib import Path

from dotenv import load_dotenv

SRC_DIR = Path(Path(__file__).parent.parent)
sys.path.insert(0, str(SRC_DIR))

from src.utils import S3Utils
from src.extract import Extractor


def test_Extractor(test_data_dir):
    """
    Test the Extractor class for querying the NewsAPI and persisting
    results as JSON files to an S3 bucket.
    """

    #load_dotenv(str(env_file))

    bucket_name = os.getenv("S3_BUCKET_NAME")

    country = "United Kingdom"

    extractor = Extractor(country)
    extractor.query()

    api_results = extractor.responses

    assert country in api_results.keys()
    assert isinstance(api_results[country], list)

    metadata_file = extractor.persist_to_s3(test_data_dir)

    metadata = S3Utils.json_to_dict(bucket_name, metadata_file)

    assert country in metadata.keys()

    # Clean-up
    S3Utils.delete_object(bucket_name, metadata[country])
    S3Utils.delete_object(bucket_name, (test_data_dir + "/" + "METADATA.json"))
