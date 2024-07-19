###################################################################
#
# Mothership Scraper Class
#
###################################################################

from .scraper import Scrapers
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime, timedelta

class MothershipScraper(Scrapers):
    """Implementation of the Mothership Scraper.
    
    Attributes:
        data: A list of data for bs4.
        headers: The header used for web scraping.
        urls: List of URLs to scrape.
        html: Base URL
    """

    def __init__(self) -> None:
        """Initialize the Mothership Class."""

        self.html = 'https://mothership.sg/'
        Scrapers.__init__(self)

    def obtain_urls(self) -> list:
        """Obtain the URLs from latest news."""

        urls_list = []
        dates_list = []
        final_urls = {}

        request = requests.get(self.html, headers = self.headers)
        html = request.content
        soup = BeautifulSoup(html, 'lxml')

        for div in soup.find_all('div', {'id': 'latest-news'}):
            for span in div.find_all('span', {'class': 'publish-date'}):
                dates_list.append(span.text)
            for a in div.find_all('a'):
                urls_list.append(a['href'])
        
        for index, item in enumerate(dates_list):
            url = urls_list[index]
            if not (url in final_urls):
                final_urls[url] = item
        
        return final_urls
    
    def crawl(self) -> None:
        """Crawl through the urls list."""

        for item in self.urls:
            request = requests.get(item)
            html = request.content
            soup = BeautifulSoup(html, 'lxml')
            self.data.append(soup)