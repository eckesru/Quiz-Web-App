from django.shortcuts import render, redirect
from Core.models import Frage, Benutzer, Antwort
# from .models import KLASSENNAME, Hier Models importieren!

from django.contrib.auth.decorators import login_required
# Zur Umleitung auf /login/ benötigt


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
def dashboard_view(request):
    frage = Frage.objects.all()

    # Sortierung des QuerySets. "-" bedeutet absteigend, "" aufsteigend.
    frage.order_by("-likes", "-creation_date")

    context = {"frage": frage, }
    return render(request, 'startseite.html', context)
    # TODO: Name der HTML-Datei anpassen.
