# from django.http import JsonResponse

from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from rest_framework.exceptions import Throttled
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST,
)
from stackoverflow.utils import (
  AnonymousPerDayThrottle, AnonymousPerMinThrottle
)
from question.helpers import search_questions, paginate_objects

class QuestionListView(APIView):
    throttle_classes = [AnonymousPerDayThrottle, AnonymousPerMinThrottle]
    permission_classes = [AllowAny]
    
    def throttled(self, request, wait):
        raise Throttled(detail={
            "message": "request limit exceeded",
            "availableIn": f"{wait} seconds",
            "throttleType": "Anonymous User"
        })

    def get(self, request, format=None):
        context = {
            'data': 'noting here'
        }
        return Response(context)

    
    # def get(self, request, *args, **kwargs):
    #     # response = search_questions(request.GET)

    #     return JsonResponse({'questions': 'response'})
