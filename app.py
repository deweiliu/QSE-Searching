import boto3
import yaml
from boto3.dynamodb.conditions import Key, Attr

with open('credentials.yml', 'r') as f:
    credentials = yaml.safe_load(f)
session = boto3.Session(aws_access_key_id=credentials['aws_access_key_id'],
                        aws_secret_access_key=credentials['aws_secret_access_key'],
                        aws_session_token=credentials['aws_session_token'],
                        region_name=credentials['region_name'])

dynamodb = session.resource('dynamodb')
table = dynamodb.Table('Indexing')
item=table.scan( FilterExpression = Attr('title').eq('Adobe Photoshop - Wikipedia'))['Items']
print(type(item))
print(len(item))
print(item)