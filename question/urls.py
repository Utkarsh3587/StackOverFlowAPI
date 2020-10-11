from django.urls import re_path

from question.views import QuestionListView

app_name = 'question'

urlpatterns = [
    re_path(r'^questions/$', QuestionListView.as_view()),
]