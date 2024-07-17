###################################################################
#
# Test Functions
#
###################################################################

from NewsAPI.newsapi import NewsAPI
import constants
from utils.utilities import save_file

def test_simple_pipeline(api_key: str) -> str:
    """Test a simple download from an API and save inside a JSON file.
    
    Attributes:
        api_key: API Key for News API.
    """

    d = NewsAPI(API_KEY)

    # Check Connection
    print(d.check_connection())

    # Download data
    parameters = {'q': 'bitcoin'}
    data = d.search('everything', parameters)

    # Save file
    filepath = '/Users/chrissastropranoto/Desktop/Seismic/etl_pipeline/data/test.json'

    save_file(data, filepath)

if __name__ == "__main__":

    # Test simple pipeline.
    # test_simple_pipeline(API_KEY)
    # print("Simple Pipeline Testing Successful.")

    # Test 





