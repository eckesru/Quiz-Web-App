from django.urls import path
from . import views

urlpatterns = [
    path("", views.antwort_edit_view, name="antwort-edit"),
]
