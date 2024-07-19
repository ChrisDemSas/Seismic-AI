###################################################################
#
# Utility Functions
#
###################################################################

import json
import os
import pandas as pd
import time
from datetime import datetime, timedelta

def save_file(data: dict, filepath: str, indent: int = 4) -> None:
    """Take in a data and a filepath, and then save the data in a filepath.
    
    Attributes:
        data: json or DataFrame
        filepath: Filepath of place to save.
        indent: indent for the json file
    """

    with open(filepath, 'w') as file:
        json.dump(data, file, indent = indent)

def read_file(filepath: str) -> json.dumps:
    """Take in a filepath and read file.
    
    Attributes:
        filepath: Filepath of json file.
    """

    if '.json' in filepath:
        f = open(filepath)
        data = json.load(f)
        f.close()
    elif '.csv' in filepath:
        data = pd.read_csv(filepath)

    return data

def _convert_datetime_mothership(date: str) -> datetime:
    """Take in a date and return a datetime.
    
    Attributes:
        dates: A date coming from Mothership.
    """

    return datetime.strptime(date, '%B %d, %Y, %H:%M %p')

def convert_datetime(date: str, source: str) -> datetime:
    """Take in a date and a source and return a datetime.
    
    Attributes:
        date: A date coming from a source.
        source: A source (Mothership, CNA, etc.)
    """

    if source == 'Mothership':
        return _convert_datetime_mothership(date)