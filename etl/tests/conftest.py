from pathlib import Path

import pytest


@pytest.fixture
def test_data_dir() -> str:
    """
    Directory path in S3 bucket for storing data produced
    during tests.
    """

    return "etl-tests-data"
