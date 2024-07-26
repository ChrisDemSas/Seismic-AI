###################################################################
#
# Google BigQuery Client Class
#
###################################################################

import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

class BigQueryClient:
    """Implementation of the BigQuery class.
    
    Attributes:
        credentials: A filepath to a file containing the credentials to connect to BigQuery.
        client: Client connecting to BigQuery.
    """

    def __init__(self, credentials: str) -> None:
        """Initialize the BigQuery class.
        
        Attributes:
            credentials: A filepath to a file containing the credentials to connect to BigQuery.
            client: Client connecting to BigQuery.
        """

        self.credentials = service_account.Credentials.from_service_account_file(credentials)
        self.client = bigquery.Client(credentials = self.credentials)

    def query(self, query: str) -> pd.DataFrame:
        """Take in a query and query the Google BigQuery database.
        
        Attributes:
            query: An SQL query.
        """

        query_job = self.client.query(query)

        return query_job.to_dataframe()
    
    def load(self, dataframe: pd.DataFrame, table_id: str) -> None:
        """Take in a dataset and load it into Google Bigquery.

        Attributes:
            data: A dataset in pandas DataFrame format.
            table_id: A Table ID which is one of the tables in the BigQuery Tables.
        """

        job = self.client.load_table_from_dataframe(dataframe, table_id)
        result = job.result()

        return result



    

