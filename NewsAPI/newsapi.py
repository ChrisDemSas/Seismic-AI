###################################################################
#
# News API Class
#
###################################################################

import requests
import pandas as pd
import boto3
import json

class NewsAPI:
    """Implementation of the News API class.
    
    Attributes:
        api_key: API Key of the NewsAPI Org.
        data: Data obtained from using the NewsAPI API.
        dataframe: Data cleaned for loading to csv.
    """

    def __init__(self, api_key: str) -> None:
        """Initialize the NewsAPI class.

        Attributes:
            api_key: API Key from newsapi.org
        """

        self.api_key = api_key
        self.data = []
        self.dataframe = {}
    
    def check_connection(self) -> str:
        """Check to see if connection is available."""

    def _construct_url(self, endpoints: str, parameters: dict) -> str:
        """Take in endpoints and parameters to construct a URL.
        
        Attributes:
            endpoints: An endpoint, either 'everythong' or 'top-headlines'.
            parameters: A dictionary of parameters.
        """
    
    def search(self, endpoints: str, parameters: dict) -> json:
        """Take in endpoints and parameters to return the data.
        
        Attributes:
            endpoints: An endpoint, either 'everythong' or 'top-headlines'.
            parameters: A dictionary of parameters.
        """

