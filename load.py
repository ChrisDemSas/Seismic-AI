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

def upload_to_s3(parameters: dict, client: aws.AWSClient, html: bool = True, csv: bool = True) -> None:
    """Take in a filepath and upload this to AWS S3.
    
    Attributes:
        filepath: The filepath of the data.
        parameters: Parameters which include: file_name, bucket, key. 
    """

    if html:
        for path in os.listdir("data/html"):
            filepath = f'data/html/{path}'
            client.upload_file(filepath, parameters)

    else:
        for path in os.listdir("data/csv"):
            filepath = f'data/csv/{path}'
            client.upload_file(filepath, parameters)


def upload_to_bigquery(parameters: dict, client: ) -> None:
    """Take in a filepath and upload this to BigQuery.
    
    Attributes:
        filepath: The filepath of the data.
    """

print(upload_to_s3('s', {'s': 1}, None))