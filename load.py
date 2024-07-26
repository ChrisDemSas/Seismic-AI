###################################################################
#
# Load Functions
#
###################################################################

import pandas as pd
import os
import utils.utilities as ut
import utils.aws as aws
import utils.bigquery as bq
from typing import Any

def upload_to_s3(client: aws.AWSClient, parameters: dict, filetype: str) -> None:
    """Take in a filepath and upload this to AWS S3.
    
    Attributes:
        filepath: The filepath of the data.
        parameters: Parameters which include: file_name, bucket, key. 
        filetype: csv or html
    """

    if filetype == 'html':
        for path in os.listdir("data/html"):
            filepath = f'data/html/{path}'
            client.upload_file(filepath, parameters)
            ut.delete_file(filepath)

    elif filetype == 'csv':
        for path in os.listdir("data/csv"):
            filepath = f'data/csv/{path}'
            client.upload_file(filepath, parameters)
            ut.delete_file(filepath)

def upload_to_bigquery(client: bq.BigQueryClient, dataframe: pd.DataFrame, table_id: str) -> None:
    """Take in a filepath and upload this to BigQuery.
    
    Attributes:
        filepath: The filepath of the data.
        dataframe: A Pandas DataFrame.
        table_id: Table ID of Bigquery
    """

    result = client.load(dataframe, table_id)

def save_locally(data: Any, filepath: str, filetype: str) -> None:
    """Take in a piece of data and save locally.
    
    Attributes:
        data: A data that is to be saved
        filepath: A filepath of where the data should be saved
        filetype: The filetype (csv or html)
    """

    ut.save_file(data, filepath, filetype)




