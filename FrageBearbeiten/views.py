from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from Core.models import Frage, Benutzer
# from .models import KLASSENNAME, Hier Models importieren!

from django.contrib.auth.decorators import login_required
# Zur Umleitung auf /login/ benötigt


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
# Create your views here.
def frage_edit_view(request, frage_id):
    frage = Frage.objects.get(id=frage_id)

    context = {"frage": frage}
    return render(request, 'frage_bearbeiten.html', context)