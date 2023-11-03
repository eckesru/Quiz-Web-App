from django.shortcuts import render, redirect
from Core.models import Frage
# from .models import KLASSENNAME, Hier Models importieren!

from django.contrib.auth.decorators import login_required
# Zur Umleitung auf /login/ benötigt


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
# Create your views here.
def meine_inhalte_view(request):
    user = request.user
    if request.method == 'POST':
        if request.POST.get("BUTTONNAME"):
            pass
        return redirect("/frage-erstellen/")
    user_fragen = Frage.objects.filter(user_id=user)
    context = {"fragen": user_fragen}
    return render(request, 'meineInhalte.html', context)
