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
    user = request.user
    frage = Frage.objects.get(id=frage_id)
    frage_user = frage.user

    if frage_user != user:
        return redirect("/frage/" + str(frage_id) + "/")
    
    if request.method == 'POST':
        # Prüfen, ob es sich bei dem Aufruf um POST handelt
        frage_text_new = request.POST.get('frageText')
        Frage.objects.filter(id=frage_id).update(text=frage_text_new)
        return redirect("/frage/" + str(frage_id) + "/")
    
    context = {"frage": frage}
    return render(request, 'frage_bearbeiten.html', context)

