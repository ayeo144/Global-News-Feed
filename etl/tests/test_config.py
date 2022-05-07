SRC_DIR = Path(Path(__file__).parent.parent)
sys.path.insert(0, str(SRC_DIR))

from src.config import Env


def test_Env_variables():

    invalid_var = ["", None]

    assert Env.NEWS_API_KEY not in invalid_var
    assert AWS_ACCESS_KEY not in invalid_var
    assert AWS_SECRET_KEY not in invalid_var
    assert S3_BUCKET_NAME not in invalid_var
    assert AWS_DB_INSTANCE_ID not in invalid_var
    assert AWS_DB_USERNAME not in invalid_var
    assert AWS_DB_PASSWORD not in invalid_var
    assert AWS_DB_HOST not in invalid_var
    assert AWS_DB_PORT not in invalid_var
    assert AWS_DB_NAME not in invalid_var
