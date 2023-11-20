from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from Core.models import Frage, Benutzer, Antwort
# from .models import KLASSENNAME, Hier Models importieren!

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
# Zur Umleitung auf /login/ benötigt


@login_required(login_url='/login/')
def frage_anzeigen_view_antwort_erstellen(request, frage_id):
    user = request.user
    frage = Frage.objects.get(id=frage_id)
    antwort_text = request.session.get('temp_antwort_text')

    # Erzeugung des Antwort-Objekts
    antwort = Antwort.objects.create(
        user=user,
        frage=frage,
        text=antwort_text
    )

    antwort.save()
    return redirect("/frage/" + str(frage_id) + "/")


@login_required(login_url='/login/')
def frage_anzeigen_view_antwort_delete(request, frage_id, antwort_id):
    user = request.user
    antwort = Antwort.objects.filter(id=antwort_id).get()
    antwort_user = antwort.user
    if antwort_user != user:
        return redirect("/frage/" + str(frage_id) + "/")
    del_user = Benutzer.objects.get(username="entfernt")
    Antwort.objects.filter(id=antwort_id).update(text="[entfernt]",
                                                 user=del_user)
    reverse_url = request.META.get("HTTP_REFERER")
    if reverse_url is None:
        return redirect("/frage/" + str(frage_id) + "/")
    return HttpResponseRedirect(reverse_url)


@login_required(login_url='/login/')
def like_antwort(request, frage_id, antwort_id):
    if request.method == 'POST':
        user = request.user
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
