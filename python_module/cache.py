from python_module.dynamoDB import *
from boto3.dynamodb.conditions import Key, Attr


def cacheDB(title):
    table = get_table('Indexing')
    response = scan(table, 'title', title, attributes=['title', 'URL','text'])
    response=response[0]
    response['text']=response['text'].replace('\n','<br/>')
    return response
