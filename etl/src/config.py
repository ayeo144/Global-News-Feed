import os

from dotenv import load_dotenv


load_dotenv()


class Env:
    """
    Store Environment variables.
    """

    NEWS_API_KEY = os.getenv("NEWS_API_KEY", None)
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", None)
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", None)
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", None)
    AWS_DB_USERNAME = os.getenv("AWS_DB_USERNAME", None)
    AWS_DB_PASSWORD = os.getenv("AWS_DB_PASSWORD", None)
    AWS_DB_HOST = os.getenv("AWS_DB_HOST", None)
    AWS_DB_PORT = os.getenv("AWS_DB_PORT", None)
    AWS_DB_NAME = os.getenv("AWS_DB_NAME", None)
