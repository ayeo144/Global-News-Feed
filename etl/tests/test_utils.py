import os
import sys
from pathlib import Path

from dotenv import load_dotenv

SRC_DIR = Path(Path(__file__).parent.parent)
sys.path.insert(0, str(SRC_DIR))

from src.utils import S3Utils


def test_S3Utils_dict_to_json(env_file, test_data_dir):
    """
    Test the upload, download and deleting of JSON data to/from
    an AWS S3 bucket.

    This test requires AWS credentials and as S3 bucket defined in
    the environment file.
    """

    load_dotenv(str(env_file))

    test_dict = {
        "id": 1,
        "text": "some text",
        "stuff": "plus some stuff",
    }
    test_json = test_data_dir + "/" + "test.json"

    # upload to S3
    S3Utils.dict_to_json(test_dict, os.getenv("S3_BUCKET_NAME"), test_json)

    # download from S3
    dict_from_s3 = S3Utils.json_to_dict(os.getenv("S3_BUCKET_NAME"), test_json)

    # delete test object
    S3Utils.delete_object(os.getenv("S3_BUCKET_NAME"), test_json)

    assert dict_from_s3 == test_dict
