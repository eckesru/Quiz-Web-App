from django.shortcuts import render
from Core.models import Frage, Benutzer
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncDate
from .utils import get_hot_frage, get_frage_des_tages, get_top_5_users


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
def startseite_view(request):

    del_user = Benutzer.objects.get(username="entfernt")

    # Sortierung des QuerySets. "-" bedeutet absteigend, "" aufsteigend.
    # TruncDate von Django holt nur Date, ignoriert Time.
    frage = Frage.objects.\
        exclude(user=del_user).\
        annotate(creation_date_only=TruncDate('creation_date')).\
        order_by("-creation_date_only", "-likes")

    hot_frage = get_hot_frage()

    frage_des_tages = get_frage_des_tages(request.user)

    top_5_user = get_top_5_users()

    context = {"frage": frage,
               "hot_frage": hot_frage,
               "frage_des_tages": frage_des_tages,
               "top_5_user": top_5_user}

    return render(request, 'startseite.html', context)
