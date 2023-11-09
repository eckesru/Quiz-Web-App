from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from Core.models import Frage, Benutzer, Antwort
# from .models import KLASSENNAME, Hier Models importieren!

from django.contrib.auth.decorators import login_required
# Zur Umleitung auf /login/ benötigt


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
# Create your views here.
def frage_anzeigen_view(request, frage_id):
    if request.method == "POST":
        # Falls der antwortErstellen-Button betätigt wurde, dann Antwort-Func.
        if 'antwortErstellen' in request.POST:
            antwort_erstellen_(request=request, frage_id=frage_id)

    frage = Frage.objects.get(id=frage_id)
    antwort = Antwort.objects.filter(frage=frage).values()
    context = {"frage": frage,
               "antwort": antwort}
    print(antwort)
    return render(request, 'frage_anzeigen.html', context)


@login_required(login_url='/login/')
def frage_anzeigen_view_delete(request, frage_id):
    user = request.user
    frage = Frage.objects.get(id=frage_id)
    frage_user = frage.user
    if frage_user != user:
        return redirect("/frage/" + str(frage_id) + "/")
    del_user = Benutzer.objects.get(username="entfernt")
    Frage.objects.filter(id=frage_id).update(title="[entfernt]",
                                             text="[entfernt]",
                                             user=del_user)
    reverse_url = request.META.get("HTTP_REFERER")
    if reverse_url is None:
        return redirect("/frage/" + str(frage_id) + "/")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def antwort_erstellen_(request, frage_id):
    user = request.user
    frage = Frage.objects.get(id=frage_id)
    antwort_text = request.POST.get('antwortText')

    # Erzeugung des Antwort-Objekts
    antwort = Antwort.objects.create(
        user=user,
        frage=frage,
        text=antwort_text
    )

    antwort.save()
    return redirect("/frage/" + str(frage_id) + "/")
