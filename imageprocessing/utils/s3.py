import boto3
from pathlib import Path

def download_file(bucket: str, file: str, destination: str, skip_if_already_exists: bool=True) -> None: 
    if skip_if_already_exists and Path(destination).exists():
        return
    
    client = boto3.client('s3')
    client.download_file(bucket, file, destination)


def upload_file(bucket:str, file: str, filename_in_bucket: str=None) -> None:
    client = boto3.client('s3')
    client.upload_file(bucket, file, filename_in_bucket)
