# Datei zur Auslagerung von Methoden
from .models import Frage, Antwort, Benutzer


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
        frage_likes += frage.likes

    antwort_likes = 0
    for antwort in antworten:
        antwort_likes += antwort.likes

    likes_amount = frage_likes + antwort_likes

    # Gewichte der Punkteberechnung
    frage_mutiplier = 2
    antwort_multiplier = 1
    like_multiplier = 3

    # Berechnung der einzelnen Punkte anhand der Gewichte
    frage_points = fragen_amount * frage_mutiplier
    antwort_points = antworten_amount * antwort_multiplier
    like_points = likes_amount * like_multiplier

    # Gesamtsumme der Punkte als Ergebnis zurückgeben
    points = frage_points + antwort_points + like_points

    # Punkte des Users in der DB aktualisieren
    Benutzer.objects.filter(id=user.id).update(_points=points)
