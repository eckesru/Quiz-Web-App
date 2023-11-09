from django.urls import path
from . import views

urlpatterns = [
    path("", views.frage_edit_view, name="frage-edit"),
]
