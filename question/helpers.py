import requests
import time

from datetime import datetime


def get_int(value):
    try:
        return int(value)
    except TypeError:
        return None
    except ValueError:
        return None


def get_boolean(value):
    if value in ['True', 'true']:
        return True
    else:
        return False


def get_sorting_order(value):
    if value == 'votes':
        return 'votes'
    elif value == 'creation':
        return 'creation'
    elif value == 'relevance':
        return 'relevance'
    else:
        return 'activity'


def search_questions(params={}):
    url = 'https://api.stackexchange.com/2.2/search/advanced?\
        key=U4DMV*8nvpm3EOpvf69Rxw((&site=stackoverflow&order=desc&filter=default'

    if params.get('sort'):
        url += "&sort={}".format(get_sorting_order(params.get('sort')))
    
    if params.get('page') and get_int(params.get('page')):
        url += "&page={}".format(get_int(params.get('page')))
    
    if params.get('pagesize', 10) and get_int(params.get('pagesize')):
        url += "&pagesize={}".format(get_int(params.get('pagesize')))
    
    if params.get('fromdate') and get_int(params.get('fromdate')):
        fromdate = int(str(time.mktime(
          datetime.datetime.strptime(params['fromdate'], "%d/%m/%Y").timetuple())).split('.')[0])
        url += "&fromdate={}".format(get_int(fromdate))

    # if params.get('min') and get_int(params.get('min')):
    #     minn = int(str(time.mktime(
    #       datetime.datetime.strptime(params['min'], "%d/%m/%Y").timetuple())).split('.')[0])
    #     url += "&min={}".format(get_int(minn))

    # if params.get('max') and get_int(params.get('max')):
    #     maxx = int(str(time.mktime(
    #       datetime.datetime.strptime(params['max'], "%d/%m/%Y").timetuple())).split('.')[0])
    #     url += "&max={}".format(get_int(maxx))
    
    if params.get('min') and get_int(params.get('min')):
        url += "&min={}".format(get_int(params.get('min')))

    if params.get('max') and get_int(params.get('max')):
        url += "&max={}".format(get_int(params.get('max')))
    
    if params.get('todate') and get_int(params.get('todate')):
        todate = int(str(time.mktime(
          datetime.datetime.strptime(params['todate'], "%d/%m/%Y").timetuple())).split('.')[0])
        url += "&todate={}".format(get_int(todate))
    
    if params.get('q'):
        url += "&q={}".format(params.get('q'))
    
    if params.get('accepted') and get_boolean(params.get('accepted')):
        url += "&accepted={}".format(params.get('accepted'))

    if params.get('answers') and get_int(params.get('answers')):
        url += "&answers={}".format(params.get('answers'))
    
    if params.get('body'):
        url += "&body={}".format(params.get('body'))
    
    if params.get('closed') and get_boolean(params.get('closed')):
        url += "&closed={}".format(params.get('closed'))

    
    if params.get('migrated') and get_boolean(params.get('migrated')):
        url += "&migrated={}".format(params.get('migrated'))
    
    if params.get('notice') and get_boolean(params.get('notice')):
        url += "&notice={}".format(params.get('notice'))
    
    if params.get('nottagged'):  #  a semicolon delimited list of tags
        url += "&nottagged={}".format(';'.join(params.get('nottagged')))

    if params.get('tagged'):  #  a semicolon delimited list of tags
        url += "&tagged={}".format(';'.join(params.get('tagged')))
    
    if params.get('title'):
        url += "&title={}".format(params.get('title'))
    
    if params.get('user') and get_int(params.get('user')):
        url += "&user={}".format(params.get('user'))

    if params.get('url'):
        url += "&url={}".format(params.get('url'))
    
    if params.get('views') and get_int(params.get('views')):
        url += "&views={}".format(params.get('views'))
    
    if params.get('wiki') and get_boolean(params.get('wiki')):
        url += "&wiki={}".format(params.get('wiki'))

    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    
    return None