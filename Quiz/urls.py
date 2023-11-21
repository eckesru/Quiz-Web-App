from django.urls import path
from .views import welcome_page, quiz_page, quiz_result

app_name = 'quiz'

urlpatterns = [
    path('', welcome_page, name='welcome_page'),
    path('<int:category_id>/', quiz_page, name='quiz_page'),
    path('<int:category_id>/result/', quiz_result, name='quiz_result'),
]