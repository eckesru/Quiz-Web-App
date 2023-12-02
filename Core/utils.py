# Datei zur Auslagerung von Methoden
from .models import Frage, Antwort, Benutzer, BenutzerQuesModel


def update_points_for_user(user):
    # Alle Fragen und Antworten des Users holen
    fragen = Frage.objects.filter(user=user)
    antworten = Antwort.objects.filter(user=user)

    # Anzahl der Fragen und Antworten berechnen
    fragen_amount = fragen.count()
    antworten_amount = antworten.count()

    # Anzahl der Likes für Fragen und Antworten berechnen, dann Summieren
    frage_likes = 0
    for frage in fragen:
        frage_likes += (frage.likes - 1)

    antwort_likes = 0
    for antwort in antworten:
        antwort_likes += (antwort.likes - 1)

    likes_amount = frage_likes + antwort_likes

    # Ermittlung der korrekten Antworten bei teilgenommenen Frage des Tages
    teilnahmen_frage_des_tages = BenutzerQuesModel.objects.filter(user=user)
    correct_answers = 0
    for teilnahme in teilnahmen_frage_des_tages:
        if (teilnahme.answer == teilnahme.quizfrage.ans):
            correct_answers += 1

    # Ermittlung der korrekten Antworten bei Quiz der Woche
    # TODO: Punktermittlung zur Quiz der Woche implementieren
    correct_quiz_answers = 0

    # Gewichte der Punkteberechnung
    frage_mutiplier = 2
    antwort_multiplier = 1
    like_multiplier = 3
    frage_des_tages_multiplier = 2
    quiz_der_woche_multiplier = 0.5

    # Berechnung der einzelnen Punkte anhand der Gewichte
    frage_points = fragen_amount * frage_mutiplier
    antwort_points = antworten_amount * antwort_multiplier
    like_points = likes_amount * like_multiplier
    frage_des_tages_points = correct_answers * frage_des_tages_multiplier
    quiz_der_woche_points = round(correct_quiz_answers *
                                  quiz_der_woche_multiplier)

    # Gesamtsumme der Punkte als Ergebnis zurückgeben
    points = frage_points + antwort_points + like_points +\
        frage_des_tages_points + quiz_der_woche_points

    # Rang des Nutzers ermitteln
    rank = get_rank(points)

    # Punkte des Users in der DB aktualisieren
    Benutzer.objects.filter(id=user.id).update(_points=points, _rank=rank)


def get_rank(points):

    rangstufen = [
        (10000, "Legende der Lehrbücher"),
        (5000,  "Professor der Problemlösung"),
        (2500,  "Doktor der Diskussion"),
        (1200,  "Gelehrter Guru"),
        (600,   "Fanatischer Forscher"),
        (300,   "Wächter des Wissens"),
        (150,   "Akademischer Adept"),
        (75,    "Begeisterter Bücherwurm"),
        (30,    "Ehrgeiziger Akademiker"),
        (0,     "Neugieriger Student")
    ]

    for boundary, rank in rangstufen:
        if points >= boundary:
            return rank
