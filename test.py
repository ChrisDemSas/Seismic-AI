###################################################################
#
# Test Functions
#
###################################################################

from NewsAPI.newsapi import NewsAPI
import constants
from utils.utilities import save_file, read_file
from transform import *

def test_simple_pipeline(api_key: str) -> str:
    """Test a simple download from an API and save inside a JSON file.
    
    Attributes:
        api_key: API Key for News API.
    """

    d = NewsAPI(api_key)

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

    # Test Transform

    #filepath = '/Users/chrissastropranoto/Desktop/Seismic/etl_pipeline/data/test.json'
    #file = read_file(filepath)

    #dataset = process_data(file)
    #fact_table, sources, meta, content = split(dataset)

    #content = summarize_content(content.iloc[:3], 'bart', min_length = 50, max_length = 100)

    #print(content['content'])










