from django.shortcuts import render
from Core.models import Frage, Benutzer, Antwort
from Quiz.models import QuesModel
from django.contrib.auth.decorators import login_required
import random
from datetime import datetime


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
def startseite_view(request):
    del_user = Benutzer.objects.get(username="entfernt")

    frage = Frage.objects.all().exclude(user=del_user)

    # Sortierung des QuerySets. "-" bedeutet absteigend, "" aufsteigend.
    frage.order_by("-likes", "-creation_date")

    hot_frage = get_hot_question()

    frage_des_tages = get_frage_des_tages(request.user)

    context = {"frage": frage,
               "hot_frage": hot_frage,
               "frage_des_tages": frage_des_tages}
    return render(request, 'startseite.html', context)
    # TODO: Name der HTML-Datei anpassen.


def get_hot_question():

    del_user = Benutzer.objects.get(username="entfernt")
    fragen = Frage.objects.all().exclude(user=del_user)

    # Aufsteigend nach Anzahl der Antworten sortieren (Fremdschlüssel),
    # dannach nach creation_date
    sorted_fragen = sorted(fragen,
                           key=lambda frage:
                           (get_antwort_count_for_frage(frage),
                            frage.creation_date),
                           reverse=False)

    return sorted_fragen[0]


def get_antwort_count_for_frage(frage):
    del_user = Benutzer.objects.get(username="entfernt")
    antwort_count = Antwort.objects.exclude(user=del_user) \
        .filter(frage=frage).count()
    return antwort_count


def get_frage_des_tages(user):
    today = datetime.now()

    # Seed definieren, welcher sich nur täglich ändert
    seed = today.day * today.month * today.year

    # Random mit dem berechneten seed initialisieren
    random.seed(seed)

    question_list = QuesModel.objects.filter(category=user.study_area)

    # Zufällige Quiz-Frage (gemäß Seed) aus der Liste wählen
    frage_des_tages = random.choice(question_list)

    return frage_des_tages
