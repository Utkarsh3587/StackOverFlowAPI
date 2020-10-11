import requests

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


def search_questions(params={}):
    url = 'https://api.stackexchange.com/2.2/search/advanced?\
        key=U4DMV*8nvpm3EOpvf69Rxw((&site=stackoverflow&\
                order=desc&sort=activity&filter=default'
    # &min=1601856000&max=1602288000
    if params.get('page', 1):
        url += "&page={}".format(params.get('page', 1))
    if params.get('pagesize', 10):
        url += "&pagesize={}".format(params.get('pagesize', 10))
    if params.get('fromdate'):
        url += "&fromdate={}".format(params.get('fromdate'))
    if params.get('todate'):
        url += "&todate={}".format(params.get('todate'))
    if params.get('q'):
        url += "&q={}".format(params.get('q'))
    if params.get('accepted'):
        url += "&accepted={}".format(params.get('accepted'))

    if params.get('answers'):
        url += "&answers={}".format(params.get('answers'))
    if params.get('body'):
        url += "&body={}".format(params.get('body'))
    if params.get('closed'):
        url += "&closed={}".format(params.get('closed'))

    if params.get('migrated'):
        url += "&migrated={}".format(params.get('migrated'))
    if params.get('notice'):
        url += "&notice={}".format(params.get('notice'))
    if params.get('nottagged'):
        url += "&nottagged={}".format(params.get('nottagged'))

    if params.get('tagged'):
        url += "&tagged={}".format(params.get('tagged'))
    if params.get('title'):
        url += "&title={}".format(params.get('title'))
    if params.get('user'):
        url += "&user={}".format(params.get('user'))

    if params.get('url'):
        url += "&url={}".format(params.get('url'))
    if params.get('views'):
        url += "&views={}".format(params.get('views'))
    if params.get('wiki'):
        url += "&wiki={}".format(params.get('wiki'))
        
    
    response = requests.get(url)
    print(response.status_code)
    questions = response.json()['items']
    return questions


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