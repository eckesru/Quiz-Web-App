# Datei zur Auslagerung von Methoden
from Core.models import Benutzer, Frage, Antwort
from Quiz.models import QuesModel
import random
from django.utils import timezone


def get_hot_frage():

    del_user = Benutzer.objects.get(username="entfernt")
    fragen = Frage.objects.all().exclude(user=del_user)

    # Frage in Liste hinzufügen, wenn keine Antworten gibt (Fremdschlüssel)
    fragen_ohne_antworten = [frage for frage in fragen
                             if get_antwort_count_for_frage(frage) == 0]

    # Aufsteigend nach creation_date sortieren
    sorted_fragen = sorted(fragen_ohne_antworten,
                           key=lambda frage:
                           frage.creation_date,
                           reverse=False)

    return sorted_fragen[0]


def get_antwort_count_for_frage(frage):
    del_user = Benutzer.objects.get(username="entfernt")
    antwort_count = Antwort.objects.exclude(user=del_user) \
        .filter(frage=frage).count()
    return antwort_count


def get_frage_des_tages(user):
    today = timezone.now()

    # Seed definieren, welcher sich nur täglich ändert
    seed = (today.day + today.weekday()) * \
           (today.month + today.year) * \
           (today.year + today.weekday() - (today.month * today.day))

    # Random mit dem berechneten seed initialisieren
    random.seed(seed)

    question_list = QuesModel.objects.filter(category=user.study_area)

    # Zufällige Quiz-Frage (gemäß Seed) aus der Liste wählen
    frage_des_tages = random.choice(question_list)

    return frage_des_tages


def get_top_5_users():

    today = timezone.now()
    one_year_before = today.replace(year=today.year - 1)

    # Nur Benutzer, deren letztes Login-Datum maximal ein Jahr her ist.
    # __gte = greater than equal
    # Sortierung nach Punkten, absteigend.
    # Es werden nur die obersten 5 Ergebnisse benötigt.
    top_5_users = Benutzer.objects.filter(last_login__gte=one_year_before)\
                                  .order_by("-_points")[:5]

    return top_5_users
