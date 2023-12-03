from django.urls import path
from .views import welcome_page, quiz_page, quiz_result, weekly_quiz_page, weekly_quiz_result

app_name = 'quiz'

urlpatterns = [
    path('', welcome_page, name='welcome_page'),
    path('weekly_quiz/', weekly_quiz_page, name='weekly_quiz_page'),
    path('weekly_quiz_result/', weekly_quiz_result, name='weekly_quiz_result'),
    path('<str:shortname>/', quiz_page, name='quiz_page'),
    path('<str:shortname>/result/', quiz_result, name='quiz_result'), 
]