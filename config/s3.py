import boto3
from botocore.exceptions import ClientError
from config import get_config

config = get_config()


class S3Client:
    def __init__(self):
        self.client = boto3.client(
            's3',
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
            region_name=config.AWS_REGION
        )
        self.bucket_name = config.S3_BUCKET_NAME
    
    def upload_file(self, file_path, object_name=None):
        if object_name is None:
            object_name = file_path
        
        try:
            self.client.upload_file(file_path, self.bucket_name, object_name)
            return True
        except ClientError as e:
            print(f"Error uploading file to S3: {e}")
            return False
    
    def upload_fileobj(self, file_obj, object_name):
        try:
            self.client.upload_fileobj(file_obj, self.bucket_name, object_name)
            return True
        except ClientError as e:
            print(f"Error uploading file object to S3: {e}")
            return False
    
    def download_file(self, object_name, file_path):
        try:
            self.client.download_file(self.bucket_name, object_name, file_path)
            return True
        except ClientError as e:
            print(f"Error downloading file from S3: {e}")
            return False
    
    def get_file_url(self, object_name, expiration=3600):
        try:
            url = self.client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': object_name},
                ExpiresIn=expiration
            )
            return url
        except ClientError as e:
            print(f"Error generating presigned URL: {e}")
            return None
    
    def delete_file(self, object_name):
        try:
            self.client.delete_object(Bucket=self.bucket_name, Key=object_name)
            return True
        except ClientError as e:
            print(f"Error deleting file from S3: {e}")
            return False
    
    def list_files(self, prefix=''):
        try:
            response = self.client.list_objects_v2(
                Bucket=self.bucket_name,
                Prefix=prefix
            )
            if 'Contents' in response:
                return [obj['Key'] for obj in response['Contents']]
            return []
        except ClientError as e:
            print(f"Error listing files from S3: {e}")
            return []


s3_client = S3Client()
