from django.urls import path
from . import views

urlpatterns = [
    path("", views.frage_anzeigen_view_antwort_erstellen,
         name="frage-antwort"),
    path("<int:antwort_id>/like/", views.like_antwort, name="like-antwort"),
    path("<int:antwort_id>/delete/", views.frage_anzeigen_view_antwort_delete,
         name="delete-antwort"),
]
