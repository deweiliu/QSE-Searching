from python_module.dynamoDB import *


def adDB(keyword):
    table = get_table('Advertisement')

    response = scan(table, 'industry', keyword, attributes=[
                    'Advertiser', 'URL', 'industry'])

    if(len(response) == 0):
        response = scan(table, 'industry', 'N/A', attributes=[
            'Advertiser', 'URL', 'industry'])
    if(len(response) > 3):
        response = response[0:3]
    return response
