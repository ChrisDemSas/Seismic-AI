###################################################################
#
# Scraper Class
#
###################################################################

from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime, timedelta

class Scrapers:
    """Implementation of the Scraper Class.
    
    Attributes:
        data: A list of data for bs4.
        headers: The header used for web scraping.
        urls: List of URLs to scrape.
    """

    def __init__(self) -> None:
        """Initialize the Scraper class."""

        self.data = []
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0)   Gecko/20100101 Firefox/78.0", 
        "Referer": "https://www.google.com"}
        self.urls = []
    
    def return_data(self) -> list:
        """Return the contents of self.data."""

        return self.data
    
    def return_urls(self) -> list:
        """Return the URLs in self.urls."""

        return self.urls
    
    def append_url(self, url: str) -> None:
        """Append a url.
        
        Attributes:
            url: A URL
        """

        self.urls.append(url)
    
    def _obtain_urls(self) -> list:
        """Obtain the URLs from latest news. """

        raise NotImplementedError
    
    def crawl(self) -> None:
        """Crawl through the urls."""

        raise NotImplementedError

