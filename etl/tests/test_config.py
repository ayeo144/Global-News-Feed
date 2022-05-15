import sys
from pathlib import Path

import pytest

SRC_DIR = Path(Path(__file__).parent.parent)
sys.path.insert(0, str(SRC_DIR))

from src.config import Env


@pytest.mark.production
def test_Env_variables():

    invalid_var = ["", None]

    assert Env.NEWS_API_KEY not in invalid_var
    assert Env.AWS_ACCESS_KEY not in invalid_var
    assert Env.AWS_SECRET_KEY not in invalid_var
    assert Env.S3_BUCKET_NAME not in invalid_var
    assert Env.DB_USERNAME not in invalid_var
    assert Env.DB_PASSWORD not in invalid_var
    assert Env.DB_HOST not in invalid_var
    assert Env.DB_PORT not in invalid_var
    assert Env.DB_NAME not in invalid_var
