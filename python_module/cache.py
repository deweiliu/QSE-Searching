from python_module.dynamoDB import *


def cacheDB(title):
    table = get_table('Indexing')
    response = scan(table,'title', title)
    response=response[0]
    print(response['text'][1:500])
    response['text']=response['text'].replace('\n','<br/>')
    print(response['text'][1:500])
    return response
