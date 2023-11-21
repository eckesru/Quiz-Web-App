from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import QuizCategory, QuesModel, QuizResults
from datetime import datetime
from django.db.models import Max
from Core.models import Benutzer

def welcome_page(request):
    # Annahme: Der Benutzer ist angemeldet
    user_id = request.user.id

    # Hole die bereits gespielten Quizzes des Benutzers
    quiz_results = QuizResults.objects.filter(user_id=request.user.id).order_by('-when_played')

    # Hole alle verfügbaren Quiz-Kategorien
    categories = QuizCategory.objects.all()

    # Rangliste für jede Quiz-Kategorie (sortiert nach Punktzahl absteigend)
    leaderboard = []
    for category in categories:
        top_results = QuizResults.objects.filter(quiz_id=category.id).order_by('-points')[:3]  # Hier 3 für die Top 3, passe es an deine Bedürfnisse an
        for result in top_results:
            user = Benutzer.objects.get(id=result.user_id)
            leaderboard.append({
                'category_name': category.name,
                'username': user.username,
                'points': result.points,
            })

    # Erstelle eine Dictionary-Struktur, um die Daten nach Kategorien zu gruppieren
    grouped_leaderboard = {}
    for entry in leaderboard:
        category_name = entry['category_name']
        if category_name not in grouped_leaderboard:
            grouped_leaderboard[category_name] = []
        grouped_leaderboard[category_name].append(entry)

    # Sortiere die Rangliste für jede Kategorie absteigend nach Punktzahl
    for category_name, entries in grouped_leaderboard.items():
        grouped_leaderboard[category_name] = sorted(entries, key=lambda x: x['points'], reverse=True)

    return render(request, 'welcome_page.html', {'categories': categories, 'quiz_results': quiz_results, 'grouped_leaderboard': grouped_leaderboard})

def quiz_page(request, category_id):
    category = get_object_or_404(QuizCategory, pk=category_id)
    questions = QuesModel.objects.filter(category=category)

    correct_answers = 0

    if request.method == 'POST':
        for question in questions:
            user_answer = request.POST.get(f'answer_{question.id}')
            if user_answer == question.ans:
                correct_answers += 1

        # Speichere das Ergebnis in der QuizResult-Tabelle
        user_id = request.user.id  # Annahme: Der Benutzer ist angemeldet
        quiz_id = category_id  # Annahme: Die quiz_id ist die category_id

        # Hier sollte deine Logik für die Berechnung der erreichten Punkte sein
        # Ich nehme an, dass die erreichten Punkte als Variable "correct_answers" verfügbar sind

        # Erstelle ein neues QuizResult-Objekt und speichere es in der Datenbank
        quiz_result = QuizResults(
            user_id=user_id,
            quiz_id=quiz_id,
            points=correct_answers,
            when_played=datetime.now()  # Aktuelles Datum und Uhrzeit
        )
        quiz_result.save()

        # Store correct answers in the session
        request.session['correct_answers'] = correct_answers
        request.session['total_questions'] = len(questions)

        # Redirect to the quiz_result page
        return redirect('quiz:quiz_result', category_id=category_id)

    return render(request, 'quiz_page.html', {'category': category, 'questions': questions})

def quiz_result(request, category_id):
    category = get_object_or_404(QuizCategory, pk=category_id)

    # Retrieve correct answers from the session
    correct_answers = request.session.get('correct_answers', 0)
    total_questions = request.session.get('total_questions', 0)

    # Clear the session to prevent re-submission
    request.session.pop('correct_answers', None)
    request.session.pop('total_questions', None)

    return render(request, 'quiz_result.html', {'category': category, 'correct_answers': correct_answers, 'total_questions': total_questions})