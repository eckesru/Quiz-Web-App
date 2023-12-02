from django.urls import path
from . import views

urlpatterns = [
    path("", views.startseite_view, name="startseite-view"),
    path("antwort-einreichen/", views.update_answer_and_statistics, name="statistics"),
]
