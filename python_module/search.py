from python_module.dynamoDB import *

def searchDB(keyword):
    table = get_table('Indexing')
    
    response = scan(table,'title', keyword,printa=True)
    return response
