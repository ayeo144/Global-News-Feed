import sys
from pathlib import Path

SRC_DIR = Path(Path(__file__).parent.parent)
sys.path.insert(0, str(SRC_DIR))

from src.run_etl import run_extract, run_load


def main():
    """
    Run the ETL steps.
    """

    run_extract()
    run_load() 


if __name__ == "__main__":

    main()
