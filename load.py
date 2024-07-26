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

def upload_to_s3(filepath: str) -> None:
    """Take in a filepath and upload this to AWS S3.
    
    Attributes:
        filepath: The filepath of the data.
    """

def upload_to_bigquery(filepath: str) -> None:
    """Take in a filepath and upload this to BigQuery.
    
    Attributes:
        filepath: The filepath of the data.
    """