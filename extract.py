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


def extract_mothership(timing: timedelta) -> None:
    """Extract Webpages from mothership."""

    scraper = MothershipScraper()
    urls = scraper.obtain_urls()

    for item in urls:
        date = ut.convert_datetime(urls[item], 'Mothership')
        if ut.check_datetime(date): # True
            scraper.append_url(urls[item])
            

