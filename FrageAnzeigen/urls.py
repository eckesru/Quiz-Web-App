from django.urls import path
from . import views

urlpatterns = [
    path("", views.frage_anzeigen_view, name="frage"),
    path("delete/", views.frage_anzeigen_view_delete, name="frage-delete"),
    path("answer/", views.frage_anzeigen_view_antwort_erstellen,
         name="frage-answer"),
    path("like-frage/", views.like_frage, name="like-frage"),
    path("like-antwort/", views.like_frage, name="like-antwort"),
]
