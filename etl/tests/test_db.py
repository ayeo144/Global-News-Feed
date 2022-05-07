import sys
from pathlib import Path

SRC_DIR = Path(Path(__file__).parent.parent)
sys.path.insert(0, str(SRC_DIR))

from src.db import engine


def test_db_connection():

	connection = None

	try:
		connection = engine.connect()
	except Exception as e:
		raise e
	finally:
		if connection is not None:
			connection.close()