import requests

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

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
    # &min=1601856000&max=1602288000
    if params.get('sort'):
        url += "&sort={}".format(get_sorting_order(params.get('sort')))
    
    if params.get('page') and get_int(params.get('page')):
        url += "&page={}".format(get_int(params.get('page')))
    
    if params.get('pagesize', 10) and get_int(params.get('pagesize')):
        url += "&pagesize={}".format(get_int(params.get('pagesize')))
    
    if params.get('fromdate'):
        url += "&fromdate={}".format(params.get('fromdate'))
    
    if params.get('todate'):
        url += "&todate={}".format(params.get('todate'))
    
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
    
    if params.get('nottagged'):
        url += "&nottagged={}".format(params.get('nottagged'))

    if params.get('tagged'):
        url += "&tagged={}".format(params.get('tagged'))
    
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
        return response.json()['items']
    
    return None


def paginate_objects(responses, page, page_size, field_name='results'):
    page = int(page)
    paginator = Paginator(responses, int(page_size))
    try:
        responses = paginator.page(page)
    except PageNotAnInteger:  # If page is not an integer, deliver first page.
        responses = paginator.page(1)
        page = 1
    except EmptyPage:
        responses = []
    # serializer = serializer_class(responses, many=True)
    json_object = {
        field_name: responses, 'per_page': paginator.per_page,
        'total': paginator.count, 'page': page
        }
    return json_object