from django.shortcuts import render, redirect
from Core.models import Frage
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
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
