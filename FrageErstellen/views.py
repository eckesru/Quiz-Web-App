from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# from .models import KLASSENNAME # Hier Model importieren!
from Core.models import Frage


# Create your views here.
def frage(request):
    if request.method == 'POST': # Prüfen, ob es sich bei dem Aufruf um POST handelt
        user = request.user
        tags = request.POST.get('frageTag')
        module = request.POST.get('frageModul')
        title = request.POST.get('frageTitel')
        text = request.POST.get('frageText')
        frage = Frage(user=user, _tags=tags, module=module, title=title, text=text)
        Frage.save(frage)
        return redirect("/FrageErstellen")
    return render(request, 'frage.html')
