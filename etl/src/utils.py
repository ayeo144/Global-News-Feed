import os
import json
from pathlib import Path
from typing import Union

import yaml
import boto3
import botocore.client

from src.config import Env


class S3RequestError(Exception):
    def __init__(self, message):
        super().__init__(message)


def read_config(file: Union[Path, str]) -> dict:
    with open(file) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


class AWSUtils:
    """
    Helper class for working with AWS services.
    """

    ACCESS_KEY = Env.AWS_ACCESS_KEY
    SECRET_KEY = Env.AWS_SECRET_KEY

    @classmethod
    def get_s3(cls) -> botocore.client.BaseClient:
        return cls._get_aws_session().client("s3")

    @classmethod
    def _get_aws_session(cls) -> boto3.Session:
        return boto3.Session(
            aws_access_key_id=cls.ACCESS_KEY,
            aws_secret_access_key=cls.SECRET_KEY,
        )


class S3Utils:
    """
    Helper class for interacting with AWS S3 services.
    """

    AWSUtils = AWSUtils

    @classmethod
    def dict_to_json(cls, content: dict, bucket: str, fpath: str):
        """
        Save a Python dictionary as JSON in an S3 bucket.
        """

        s3 = cls.AWSUtils.get_s3()
        response = s3.put_object(
            Body=json.dumps(content, ensure_ascii=False),
            Bucket=bucket,
            Key=fpath,
        )

        cls.validate_response(response, 200)

    @classmethod
    def json_to_dict(cls, bucket: str, fpath: str) -> dict:

        s3 = cls.AWSUtils.get_s3()
        data = s3.get_object(Bucket=bucket, Key=fpath)
        contents = data["Body"].read().decode("utf-8")

        return json.loads(contents)

    @classmethod
    def delete_object(cls, bucket: str, fpath: str):

        s3 = cls.AWSUtils.get_s3()
        response = s3.delete_object(Bucket=bucket, Key=fpath)

        cls.validate_response(response, 204)

    @staticmethod
    def validate_response(response: dict, http_code: int):
        """
        Validate the response from AWS.
        """

        status_code = response["ResponseMetadata"]["HTTPStatusCode"]
        if status_code != http_code:
            raise S3RequestError(f"Status Code = {status_code}!")
