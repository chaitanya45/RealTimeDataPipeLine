import boto3
import json
from app_config import S3_BUCKET, AWS_REGION

s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_to_s3(text, result):
    key = f"sentiment-results/{hash(text)}.json"
    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=json.dumps(result).encode("utf-8")
    )