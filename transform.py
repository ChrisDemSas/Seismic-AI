###################################################################
#
# Transformation Functions
#
###################################################################

from utils.utilities import read_file
import uuid
import pandas as pd
from Summarizers.summarizer import Summarizer

filepath = '/Users/chrissastropranoto/Desktop/Seismic/etl_pipeline/data/test.json'

file = read_file(filepath)

def process_data(file: dict) -> dict:
    """Take in the unprocessed data and return a dictionary containing the processed data.
    
    Pre-Condition: File must be in the format of a json NewsAPI download.
    """

    dataset = {
            'source': [],
            'author': [],
            'title': [],
            'description': [],
            'url': [],
            'urlToImage': [],
            'publishedAt': [],
            'content': []
            }

    for item in file['articles']:
        for heading in item:
            if heading == 'source':
                to_append = item[heading]['name']
            else:
                to_append = item[heading]
            dataset[heading].append(to_append)
    
    return dataset

def _filter(dataset: dict, columns: list[str]) -> dict:
    """Take in a dataset and filter it.
    
    Attributes:
        dataset: The dataset that is to be filtered.
        columns: Columns where the dataset has to be filtered.
    """

    filtered_dataset = {}

    for item in columns:
        filtered_dataset[item] = dataset[item]

    return filtered_dataset

def _generate_id(dataset: dict) -> dict:
    """Take in a dataset and generate UUID for each row, return the appended dataset and UUID list.
    
    Attributes:
        dataset: The dataset that is to have a UUID generated.
    """

    ids = []
    counter = 0

    len_dataset = pd.DataFrame(dataset).shape[0]

    while counter < len_dataset:
        result = uuid.uuid4()
        ids.append(result.hex)
        counter += 1

    return ids

def split(dataset: dict, length: int) -> pd.DataFrame:
    """Take in a dataset and split it into schemas:
    
    Fact Table:
        source_id
        meta_id
        content_id

    Sources Table:
        source_id
        source
        url
        urlToimage
    
    Meta Table:
        meta_id
        title
        author
        publishedAt

    Content Table:
        content_id
        description
        content (summarized content)
    
    Attributes:
        dataset: The dataset that is to be split according to the above schema.
        length: The length of the dataset.
    """

    source_table = ['source', 'url', 'urlToimage']
    meta_table = ['title', 'author', 'publishedAt']
    content_table = ['content_id', 'description', 'content']

    sources = _filter(dataset, source_table)
    meta = _filter(dataset, meta_table)
    content = _filter(dataset, content_table)

    sources['source_id'] = _generate_id(sources)
    meta['meta_id'] = _generate_id(meta)
    content['content_id'] = _generate_id(content)

    fact_table = {'source_id': sources['source_id'],
                  'meta_id': meta['meta_id'],
                  'content_id': content['content_id']}
    
    return pd.DataFrame(fact_table), pd.DataFrame(sources), pd.DataFrame(meta), pd.DataFrame(content)

def summarize_content(content: pd.DataFrame) -> pd.DataFrame:
    """Take in the contents dataframe and summarize the articles.
    
    Attributes:
        content: A dataframe containing contents of the articles.
    """





