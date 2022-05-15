import os

# from dotenv import load_dotenv


# load_dotenv()


class Env:
    """
    Store Environment variables.
    """

    NEWS_API_KEY = os.getenv("NEWS_API_KEY", None)
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", None)
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", None)
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", None)
    DB_USERNAME = os.getenv("DB_USERNAME", None)
    DB_PASSWORD = os.getenv("DB_PASSWORD", None)
    DB_HOST = os.getenv("DB_HOST", None)
    DB_PORT = os.getenv("DB_PORT", None)
    DB_NAME = os.getenv("DB_NAME", None)
