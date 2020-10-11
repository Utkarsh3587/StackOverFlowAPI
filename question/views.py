from django.http import JsonResponse

from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from question.helpers import search_questions, paginate_objects

class QuestionListView(ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        response = search_questions(request.GET)

        return JsonResponse({'questions': response})
