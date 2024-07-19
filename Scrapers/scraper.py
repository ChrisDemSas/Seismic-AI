###################################################################
#
# Scraper Class
#
###################################################################

from bs4 import BeautifulSoup

class Scrapers:
    """Implementation of the Scraper Class.
    
    Attributes:
        data: A list of data for bs4.

    """

    def __init__(self) -> None:
        """Initialize the Scraper class."""

        self.data = []
    
    def return_data(self) -> list:
        """Return the contents of self.data."""

        return self.data
    
    def _obtain_urls(self) -> list:
        """Obtain the URLs from latest news. """

        raise NotImplementedError
    
    def crawl(self) -> None:
        """Crawl through the urls."""

        raise NotImplementedError

