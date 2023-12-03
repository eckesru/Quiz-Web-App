from django.shortcuts import render, redirect, get_object_or_404
from .models import QuesModel, QuizResults, WeeklyQuizResults
from django.utils import timezone
from Core.models import Benutzer, StudyArea
import random
from django.core import serializers
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.contrib import messages
from django.urls import reverse


@login_required(login_url='/login/')
def welcome_page(request):
    # Hole die bereits gespielten Quizzes des Benutzers
    quiz_results = QuizResults.objects.filter(
        user_id=request.user.id).order_by('-when_played')

    # Hole alle verfügbaren Quiz-Kategorien
    categories = StudyArea.objects.all()

    # Rangliste für jede Quiz-Kategorie (sortiert nach Punktzahl absteigend)
    leaderboard = []
    for category in categories:
        top_results = QuizResults.objects.filter(quiz_id=category.id).order_by(
            '-points')[:10]  # Hier [:10] für die Top 10
        for result in top_results:
            user = Benutzer.objects.get(id=result.user_id)
            leaderboard.append({
                'category_name': category.name,
                'username': user.username,
                'points': result.points,
            })

    # Erstelle eine Dictionary-Struktur,
    # um die Daten nach Kategorien zu gruppieren
    grouped_leaderboard = {}
    for entry in leaderboard:
        category_name = entry['category_name']
        if category_name not in grouped_leaderboard:
            grouped_leaderboard[category_name] = []
        grouped_leaderboard[category_name].append(entry)

    # Sortiere die Rangliste für jede Kategorie absteigend nach Punktzahl
    for category_name, entries in grouped_leaderboard.items():
        grouped_leaderboard[category_name] = sorted(entries,
                                                    key=lambda x: x['points'],
                                                    reverse=True)

    return render(request, 'welcome_page.html',
                  {'categories': categories,
                   'quiz_results': quiz_results,
                   'grouped_leaderboard': grouped_leaderboard})


@login_required(login_url='/login/')
def quiz_page(request, shortname):
    category = get_object_or_404(StudyArea, shortname=shortname)

    if request.method == 'GET':
        # Seed definieren, welcher sich nur immer ändert
        now = timezone.now()
        seed = (now.hour + now.minute + now.second + now.microsecond)

        # Random mit dem berechneten seed initialisieren
        random.seed(seed)

        # Zufällige Sortierung, Limit 15.
        limit = 15
        questions = sorted(QuesModel.objects.filter(category=category),
                           key=lambda x: random.random())[:limit]

        request.session['total_questions'] = limit
        request.session['questions_quiz'] = \
            serializers.serialize('json', questions)

        return render(request, 'quiz_page.html', {'category': category,
                                                  'questions': questions})

    if request.method == 'POST':
        questions_json = request.session.get('questions_quiz')
        questions = serializers.deserialize('json', questions_json)

        correct_answers = 0
        for deserialized_question in questions:
            question = deserialized_question.object
            user_answer = request.POST.get(f'answer_{question.id}')
            if user_answer == question.ans:
                correct_answers += 1

        # Speichere das Ergebnis in der QuizResult-Tabelle
        user_id = request.user.id  # Annahme: Der Benutzer ist angemeldet
        quiz_id = category.id  # Extrahiere die ID aus dem category-Objekt

        # Hier sollte deine Logik für die Berechnung der erreichten Punkte sein
        # Ich nehme an, dass die erreichten Punkte als Variable
        # "correct_answers" verfügbar sind

        # Erstelle ein neues QuizResult-Objekt
        # und speichere es in der Datenbank
        quiz_result = QuizResults(
            user_id=user_id,
            quiz_id=quiz_id,
            points=correct_answers,
            when_played=timezone.now()  # Aktuelles Datum und Uhrzeit
        )
        quiz_result.save()

        # Store correct answers in the session
        request.session['correct_answers'] = correct_answers

        # Redirect to the quiz_result page
        return redirect(f'/quiz/{shortname}/result/')

    return redirect("/quiz/")

@login_required(login_url='/login/')
def weekly_quiz_page(request):
    now = timezone.now()
    start_of_week = now - timedelta(days=now.weekday(), hours=now.hour, minutes=now.minute, seconds=now.second, microseconds=now.microsecond)
    seed = start_of_week.isocalendar()[1]

    random.seed(seed)

    question_pool = QuesModel.objects.all()

    # Wöchentliches Quiz erstellen oder vorhandenes abrufen
    weekly_questions = random.sample(list(question_pool), min(15, len(question_pool)))

    # Überprüfen, ob der Benutzer das wöchentliche Quiz bereits gespielt hat
    user_id = request.user.id
    quiz_week = start_of_week.isocalendar()[1]

    quiz_already_played = WeeklyQuizResults.objects.filter(user_id=user_id, quiz_week=quiz_week).exists()

    if request.method == 'POST':
        if quiz_already_played:
            # Wenn der Benutzer das Quiz bereits gespielt hat, kehren Sie einfach zur weekly_quiz_page zurück
            return redirect(reverse('quiz:weekly_quiz_page'))

        user_answers = {key: request.POST[key] for key in request.POST if key.startswith('answer_')}

        correct_answers = 0
        for question in weekly_questions:
            user_answer = user_answers.get(f'answer_{question.id}')
            if user_answer == question.ans:
                correct_answers += 1

        # Speichern Sie das Ergebnis in der WeeklyQuizResults-Tabelle
        weekly_quiz_result = WeeklyQuizResults(
            user_id=user_id,
            quiz_week=quiz_week,
            points=correct_answers
        )
        weekly_quiz_result.save()

        return redirect(reverse('quiz:weekly_quiz_result'))

    return render(request, 'weekly_quiz_page.html', {'questions': weekly_questions, 'quiz_already_played': quiz_already_played})

@login_required(login_url='/login/')
def quiz_result(request, shortname):
    category = get_object_or_404(StudyArea, shortname=shortname)

    # Retrieve correct answers from the session
    correct_answers = request.session.get('correct_answers')
    total_questions = request.session.get('total_questions')

    return render(request, 'quiz_result.html',
                  {'category': category,
                   'correct_answers': correct_answers,
                   'total_questions': total_questions})


@login_required(login_url='/login/')
def weekly_quiz_result(request):
    # Holen Sie sich die Ergebnisse des aktuellen Benutzers für das aktuelle Quiz der Woche
    results = WeeklyQuizResults.objects.filter(user_id=request.user.id).order_by('-when_played')[:1]

    if not results:
        # Wenn keine Ergebnisse vorhanden sind, leiten Sie den Benutzer zu einer Fehlerseite weiter
        return render(request, 'no_quiz_result.html')

    result = results[0]

    return render(request, 'weekly_quiz_result.html', {'result': result})
