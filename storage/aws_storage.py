import boto3

from storage.base_storage import IStorage


class AWSStorage(IStorage):
    def __init__(self, secret_name, region_name="us-east-1"):
        self.secret_name = secret_name
        self.client = boto3.client('secretsmanager', region_name=region_name)
    
    def get_key(self) -> bytes:
        response = self.client.get_secret_value(SecretId=self.secret_name)
        return response['SecretString'].encode('utf-8')

    def store_key(self, key: bytes):
        self.client.put_secret_value(SecretId=self.secret_name, SecretString=key.decode('utf-8'))
