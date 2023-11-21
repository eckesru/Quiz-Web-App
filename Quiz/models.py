from django.db import models
from Core.models import Benutzer

class QuizCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class QuesModel(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    op1 = models.CharField(max_length=255)
    op2 = models.CharField(max_length=255)
    op3 = models.CharField(max_length=255)
    op4 = models.CharField(max_length=255)
    ans = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class QuizResults(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    quiz_id = models.IntegerField()
    points = models.IntegerField()
    when_played = models.DateTimeField(auto_now_add=True)

    def get_category_name(self):
        try:
            # Versuche, den Namen der Kategorie anhand der quiz_id zu bekommen
            category_name = QuizCategory.objects.get(id=self.quiz_id).name
            return category_name
        except QuizCategory.DoesNotExist:
            # Falls die Kategorie nicht gefunden wurde
            return "Unknown Category"

    def __str__(self):
        return f"Result ID: {self.id} - User: {self.user_id} - Quiz Category: {self.get_category_name()} - Points: {self.points} - Played at: {self.when_played}"