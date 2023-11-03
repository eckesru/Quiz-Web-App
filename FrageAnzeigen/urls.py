from django.urls import path
from . import views

urlpatterns = [
    path("", views.frage_anzeigen_view, name="frage"),
    path("delete/", views.frage_anzeigen_view_delete, name="frage-delete"),
    path("edit/", views.frage_anzeigen_view_edit, name="frage-edit"),
]
