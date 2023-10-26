from django.urls import path
from . import views

urlpatterns = [
    path("", views.meine_inhalte_view, name="meine-inhalte"),
]
