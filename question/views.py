import time
import datetime

from django.core.cache import cache

from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.exceptions import Throttled
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST,
)

from stackoverflow.utils import (
  AnonymousPerDayThrottle, AnonymousPerMinThrottle
)
from question.helpers import search_questions


class QuestionListView(CreateAPIView):
    throttle_classes = [AnonymousPerDayThrottle, AnonymousPerMinThrottle]
    permission_classes = [AllowAny]
    
    # handle throttle exceed 
    def throttled(self, request, wait):
        raise Throttled(detail={
            "message": "request limit exceeded",
            "availableIn": f"{wait} seconds",
            "throttleType": "Anonymous User"
        })

    def post(self, request, *args, **kwargs):   
        
        pagesize = request.data.get('pagesize', 10)

        print(request.data, "helo", "\n\n")
        
        intagg_string = 'in' + '-' + ';'.join(request.data.get('tagged', []))
        ex_tagg_string = 'ex'+'-'+';'.join(request.data.get('nottagged', []))
        other_string = "-".join([str(i) for i in request.data.values()
                                 if type(i) is not list ])
        result_string = 'results'+'-' + str(pagesize) if type(pagesize) is int else '10'
        
        cache_key = intagg_string + ex_tagg_string + other_string + result_string
        print(cache_key)
        cache_time = 86400
        data = cache.get(cache_key)
        context = {
          'message': 'data cached',
          'data': []
        }

        if data:
            context.update({'data': data})
            return Response(context, status=HTTP_200_OK)
        else:
            try:
                response = search_questions(request.data)
                questions = response['items']
                cache.set(cache_key, questions, cache_time)
                context.update({'message': 'data fetched successfully',
                                'data': questions, 'has_more': response['has_more']})
                return Response(context, status=HTTP_201_CREATED)
            except:
                context.update({'message': 'request error form StackAPi'})
                return Response(context, status=HTTP_400_BAD_REQUEST)
