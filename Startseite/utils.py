# Datei zur Auslagerung von Methoden
from Core.models import Benutzer, Frage, Antwort, BenutzerQuesModel
from Quiz.models import QuesModel
import random


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
    date = timestamp.date

    antworten_frage_des_tages = BenutzerQuesModel.objects.filter(
        date=date, frage_des_tages=frage_des_tages)

    quizfrage_answers_list = \
        [frage.answer for frage in antworten_frage_des_tages]

    op1, op2, op3, op4 = 0
    for answer in quizfrage_answers_list:
        if answer == "op1":
            op1 += 1
        elif answer == "op2":
            op2 += 1
        elif answer == "op3":
            op3 += 1
        elif answer == "op4":
            op4 += 1

    sum = op1 + op2 + op3 + op4

    if sum != 0:
        op1_stats = round(op1 / sum, 2)
        op2_stats = round(op2 / sum, 2)
        op3_stats = round(op3 / sum, 2)
        op4_stats = round(op4 / sum, 2)
    else:
        op1_stats, op2_stats, op3_stats, op4_stats = None

    return [op1_stats, op2_stats, op3_stats, op4_stats]
