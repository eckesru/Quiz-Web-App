from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from Core.models import Frage, Benutzer, Antwort
# from .models import KLASSENNAME, Hier Models importieren!

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
# Zur Umleitung auf /login/ benötigt


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
# Create your views here.
def frage_anzeigen_view(request, frage_id):
    if request.method == "POST":
        # Falls der antwortErstellen-Button betätigt wurde, dann Antwort-Func.
        if 'antwortErstellen' in request.POST:
            return redirect("/frage/" + str(frage_id) + "/" + "answer/")

    frage = Frage.objects.get(id=frage_id)
    antwort = Antwort.objects.filter(frage=frage)
    # Sortierung des QuerySets. "-" bedeutet absteigend, "" aufsteigend.
    antwort.order_by("-likes", "-creation_date")
    antwort.values()
    print(antwort)
    context = {"frage": frage,
               "antwort": antwort}
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
    return HttpResponseRedirect(reverse_url)


@login_required(login_url='/login/')
def frage_anzeigen_view_antwort_erstellen(request, frage_id):
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


@login_required(login_url='/login/')
def like_frage(request, frage_id):
    if request.method == 'POST':
        user = request.user
        frage = Frage.objects.filter(id=frage_id).get()

        if frage in user.liked_fragen.all():
            likes_new = frage.likes - 1
            Frage.objects.filter(id=frage_id).update(likes=likes_new)
            user.liked_fragen.remove(frage)
            return JsonResponse({'liked': False})

        likes_new = frage.likes + 1
        Frage.objects.filter(id=frage_id).update(likes=likes_new)
        user.liked_fragen.add(frage)
        return JsonResponse({'liked': True})

    return JsonResponse({'liked': False})


@login_required(login_url='/login/')
def like_antwort(request, frage_id):
    if request.method == 'POST':
        user = request.user
        antwort_id = request.POST.get('antwort_id')
        antwort = Antwort.objects.filter(id=antwort_id).get()

        if antwort in user.liked_antworten.all():
            likes_new = antwort.likes - 1
            Antwort.objects.filter(id=antwort_id).update(likes=likes_new)
            user.liked_antworten.remove(antwort)
            return JsonResponse({'liked': False})

        likes_new = antwort.likes + 1
        Antwort.objects.filter(id=antwort_id).update(likes=likes_new)
        user.liked_antworten.add(antwort)
        return JsonResponse({'liked': True})

    return JsonResponse({'liked': False})
