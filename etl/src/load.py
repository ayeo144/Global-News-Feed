import os
import json
import datetime
from typing import Optional

from pydantic import BaseModel


class Loader:
    """
    Load data from the extraction phase into the database.

    Data needs to be taken from the JSON files, useful content extracted
    and then loaded into a database table.

    Take metadata file created during Extract phase, read json files, add to db.
    """

    pass


class Record(BaseModel):
    """
    Data validation layer.
    """

    source: Optional[str] = None
    author: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    publish_date: Optional[datetime.datetime] = None
    country: str
