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

        url = 'https://newsapi.org/v2/everything?q=bitcoin'
        request = requests.get(url, headers = {'Authorization': self.api_key})
        status_code = request.status_code

        if status_code == 200:
            return 'Connection Successful'
        else:
            return f'Error: {status_code}'

    def _construct_url(self, endpoints: str, parameters: dict) -> str:
        """Take in endpoints and parameters to construct a URL.
        
        Attributes:
            endpoints: An endpoint, either 'everythong' or 'top-headlines'.
            parameters: A dictionary of parameters.
        """
        
        url = f'https://newsapi.org/v2/{endpoints}?'

        for item in parameters:
            url += f'{item}={parameters[item]}&'
        
        return url[:-1]

    def search(self, endpoints: str, parameters: dict) -> json:
        """Take in endpoints and parameters to return the data.
        
        Attributes:
            endpoints: An endpoint, either 'everythong' or 'top-headlines'.
            parameters: A dictionary of parameters."""
        
        url = self._construct_url(endpoints, parameters)
        request = requests.get(url, headers = {'Authorization': self.api_key})

        return request.json()