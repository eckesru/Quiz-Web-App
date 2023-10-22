from django.urls import path
from . import views

urlpatterns = [
    path("", views.frage_erstellen_view, name="frage-erstellen"),
]
