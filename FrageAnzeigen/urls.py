from django.urls import path
from . import views

urlpatterns = [
    path("", views.frage_anzeigen_view, name="frage-anzeigen"),
    path("delete/", views.frage_anzeigen_view_delete, name="frage-delete"),
    path("like/", views.like_frage, name="frage-like"),
]
