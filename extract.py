###################################################################
#
# Extract Functions
#
###################################################################

import utils.utilities as ut
from Scrapers.mothership import MothershipScraper
import json
import os
import pandas as pd
import time
from datetime import datetime, timedelta

def extract(source: str, timing: timedelta) -> list:
    """Take in a source and timing and collect the data."""

    if source == 'Mothership':
        scraper = MothershipScraper()
    else:
        raise NotImplementedError
    
    urls = scraper.obtain_urls()
    for item in urls:
        date = ut.convert_datetime(urls[item], source)
        if ut.check_datetime(date, timing): # True
            scraper.append_url(item)

    scraper.crawl()

    return scraper.return_data()