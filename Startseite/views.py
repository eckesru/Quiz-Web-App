from django.shortcuts import render
from Core.models import Frage, Benutzer
from django.contrib.auth.decorators import login_required
from .utils import get_hot_frage, get_frage_des_tages


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
def startseite_view(request):
    del_user = Benutzer.objects.get(username="entfernt")

    frage = Frage.objects.all().exclude(user=del_user)

    # Sortierung des QuerySets. "-" bedeutet absteigend, "" aufsteigend.
    frage.order_by("-likes", "-creation_date")

    hot_frage = get_hot_frage()

    frage_des_tages = get_frage_des_tages(request.user)

    context = {"frage": frage,
               "hot_frage": hot_frage,
               "frage_des_tages": frage_des_tages}
    return render(request, 'startseite.html', context)
    # TODO: Name der HTML-Datei anpassen.
