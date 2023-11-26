from django.shortcuts import render
from Core.models import Frage, Antwort
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
def meine_inhalte_view(request):
    user = request.user

    user_fragen = Frage.objects.filter(user_id=user).\
        order_by("-creation_date")

    user_antworten = Antwort.objects.filter(user_id=user).\
        order_by("-creation_date")

    context = {"fragen": user_fragen, "antworten": user_antworten}
    return render(request, 'meineInhalte.html', context)
