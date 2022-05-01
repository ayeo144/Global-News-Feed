from pathlib import Path
from typing import Union

import yaml


def read_config(file: Union[Path, str]) -> dict:
    with open(file) as f:
        return yaml.load(f, Loader=yaml.FullLoader)
