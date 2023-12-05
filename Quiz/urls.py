from django.urls import path
from .views import welcome_page, quiz_page, quiz_result, quizderwoche_page, quizderwoche_result

app_name = 'quiz'

urlpatterns = [
    path('', welcome_page, name='welcome_page'),
    path('quizderwoche/', quizderwoche_page, name='quizderwoche_page'),
    path('quizderwoche/result/', quizderwoche_result, name='quizderwoche_result'),
    path('<str:shortname>/', quiz_page, name='quiz_page'),
    path('<str:shortname>/result/', quiz_result, name='quiz_result'), 
]