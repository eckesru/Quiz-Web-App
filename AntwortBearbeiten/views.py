from django.shortcuts import render, redirect
from Core.models import Antwort
from django.contrib.auth.decorators import login_required


# Leitet User zum Login, wenn nicht eingeloggt
@login_required(login_url='/login/')
def antwort_edit_view(request, frage_id, antwort_id):
    user = request.user
    antwort = Antwort.objects.get(id=antwort_id)
    antwort_user = antwort.user

    if antwort_user != user:
        return redirect("/frage/" + str(frage_id) + "/")

    if request.method == 'POST':
        # Prüfen, ob es sich bei dem Aufruf um POST handelt
        antwort_text_new = request.POST.get('antwortText')
        Antwort.objects.filter(id=antwort_id).update(text=antwort_text_new)
        return redirect("/frage/" + str(frage_id) + "/")

    context = {"antwort": antwort}
    return render(request, 'antwort_bearbeiten.html', context)
