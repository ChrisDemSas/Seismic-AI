###################################################################
#
# AWS Client Class
#
###################################################################

import boto3

class AWSClient:
    """Implementation of the AWSClient class.
    
    Attributes:
        aws_access_key: Access Key from AWS
        aws_secret_access_key: Secret Access Key from AWS
        aws_session_token: Session Token for temporary credentials.
        service: Current AWS Service Served 
        client: Current Client
    """

    def __init__(self, aws_access_key: str, aws_secret_access_key: str, aws_session_token: str) -> None:
        """Initialize the AWSClient class.
        
        Attributes:
            aws_access_key: Access Key from AWS
            aws_secret_access_key: Secret Access Key from AWS
            aws_session_token: Session Token for temporary credentials.
        """

        self.aws_access_key = aws_access_key
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_session_token = aws_session_token
        self.service = None
        self.client = None
    
    def create_client(self, service: str) -> None:
        """Take in a service and create a client.
        Pre-Condition: Service must be an AWS service!
        
        Attributes:
            service: AWS service
        """

        self.client = boto3.client(
            service,
            aws_access_key_id = self.aws_access_key,
            aws_secret_access_key = self.aws_secret_access_key,
            aws_session_token = self.aws_session_token
        )

        self.service = service
    
    def print_service(self) -> str:
        """Print the current service."""

        if self.service is None:
            return 'No Service Recorded'
        else:
            return self.service
        
    def _s3_upload(self, filepath: str, parameters: dict) -> str:
        """Upload a piece of data into AWS S3.
        
        Attributes:
            data: The data's file path.
            parameters: Parameters which include: file_name, bucket, object_name.
        """

        bucket = parameters['bucket']
        self.client.upload_file(filepath, bucket)

    def upload_file(self, filepath: str, parameters: dict) -> None:
        """Upload a file to AWS Aurora or AWS S3.
        
        Attributes:
            filepath: The data's file path.
            parameters: Parameters which include: file_name, bucket, object_name.
        """

        if self.service == 's3':
            self._s3_upload(filepath, parameters)