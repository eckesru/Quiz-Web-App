# Datei zur Auslagerung von Methoden
from Core.models import Benutzer, Frage, Antwort, BenutzerQuesModel
from Quiz.models import QuesModel
import random
from collections import Counter


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


def get_frage_des_tages(user, timestamp):

    # Seed definieren, welcher sich nur täglich ändert
    seed = (timestamp.day + timestamp.weekday()) * \
           (timestamp.month + timestamp.year) * \
           (timestamp.year + timestamp.weekday() -
            (timestamp.month * timestamp.day))

    # Random mit dem berechneten seed initialisieren
    random.seed(seed)

    question_list = QuesModel.objects.filter(category=user.study_area)

    # Zufällige Quiz-Frage (gemäß Seed) aus der Liste wählen
    frage_des_tages = random.choice(question_list)

    return frage_des_tages


def get_top_5_users(timestamp):

    one_year_before = timestamp.replace(year=timestamp.year - 1)

    # Nur Benutzer, deren letztes Login-Datum maximal ein Jahr her ist.
    # __gte = greater than equal
    # Sortierung nach Punkten, absteigend.
    # Es werden nur die obersten 5 Ergebnisse benötigt.
    top_5_users = Benutzer.objects.filter(last_login__gte=one_year_before)\
                                  .order_by("-_points")[:5]

    return top_5_users


def get_user_answer_frage_des_tages(user, frage_des_tages, timestamp):
    date = timestamp.date()

    try:
        answer_frage_des_tages = BenutzerQuesModel.objects.\
            get(date=date,
                user=user,
                quizfrage=frage_des_tages)
    except BenutzerQuesModel.DoesNotExist:
        user_answer = None
    else:
        user_answer = answer_frage_des_tages.answer
    finally:
        return user_answer


def get_statistics_frage_des_tages(frage_des_tages, timestamp):
    date = timestamp.date()

    try:
        antworten_frage_des_tages = BenutzerQuesModel.objects.filter(
            date=date, quizfrage=frage_des_tages)

        quizfrage_answers_list = \
            [frage.answer for frage in antworten_frage_des_tages]

        # Counter: Zählt automatisch die Werte und erstellt Dictionary dazu
        counter_answers = Counter(quizfrage_answers_list)

        total = counter_answers.total()
        options = ['op1', 'op2', 'op3', 'op4']

        statistics = {key: round((counter_answers[key] / total) * 100, 2)
                      for key in counter_answers}

        # Wenn eins der op fehlt, mit Wert 0 hinzufügen
        for option in options:
            statistics.setdefault(option, 0)

    except BenutzerQuesModel.DoesNotExist or ZeroDivisionError:
        statistics = {key: 0 for key in options}

    finally:
        return statistics
