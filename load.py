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

def upload_to_s3(client: aws.AWSClient, parameters: dict, html: bool = True, csv: bool = True) -> None:
    """Take in a filepath and upload this to AWS S3.
    
    Attributes:
        filepath: The filepath of the data.
        parameters: Parameters which include: file_name, bucket, key. 
    """

    if html:
        for path in os.listdir("data/html"):
            filepath = f'data/html/{path}'
            client.upload_file(filepath, parameters)
            ut.delete_file(filepath)

    else:
        for path in os.listdir("data/csv"):
            filepath = f'data/csv/{path}'
            client.upload_file(filepath, parameters)
            ut.delete_file(filepath)

def upload_to_bigquery(client: bq.BigQueryClient, dataframe: pd.DataFrame, table_id: str) -> None:
    """Take in a filepath and upload this to BigQuery.
    
    Attributes:
        filepath: The filepath of the data.
    """

    result = client.load(dataframe, table_id)



