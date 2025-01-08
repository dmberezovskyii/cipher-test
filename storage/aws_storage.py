from abc import ABC

import boto3

from storage.base_provider import IProvider


class AWSStorage(IProvider, ABC):
    def __init__(self, secret_name, region_name="us-east-1"):
        self.secret_name = secret_name
        self.client = boto3.client("secretsmanager", region_name=region_name)