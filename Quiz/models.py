from django.db import models
from Core.models import StudyArea


class QuesModel(models.Model):
    category = models.ForeignKey(StudyArea, on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=255)
    op1 = models.CharField(max_length=255)
    op2 = models.CharField(max_length=255)
    op3 = models.CharField(max_length=255)
    op4 = models.CharField(max_length=255)
    ans = models.CharField(max_length=255)

    def __str__(self):
        return self.question

    # Hilfsmethode zur Punkteberechnung im Core (Frage des Tages)
    def get_option_by_value(self, value):
        options = {self.op1: 'op1', self.op2: 'op2',
                   self.op3: 'op3', self.op4: 'op4'}
        return options.get(value)

    class Meta:
        managed = False
        db_table = "Quiz_quesmodel"


class WeeklyQuizResults(models.Model):
    user_id = models.IntegerField()
    quiz_week = models.IntegerField()  # Kalenderwoche
    points = models.IntegerField()
    when_played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"WeeklyQuizResult ID: {self.id}\
              - User: {self.user.username}\
                 - Points: {self.points}\
                  - Played at: {self.when_played}"


class QuizResults(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    quiz_id = models.IntegerField()
    points = models.IntegerField()
    when_played = models.DateTimeField(auto_now_add=True)

    def get_category_name(self):
        try:
            # Versuche, den Namen der Kategorie anhand der quiz_id zu bekommen
            category_name = StudyArea.objects.get(id=self.quiz_id).name
            return category_name
        except StudyArea.DoesNotExist:
            # Falls die Kategorie nicht gefunden wurde
            return "Unknown Category"

    def __str__(self):
        return f"Result ID: {self.id}\
                - User: {self.user_id}\
                - Quiz Category: {self.get_category_name()}\
                - Points: {self.points}\
                - Played at: {self.when_played}"

    class Meta:
        managed = False
        db_table = "Quiz_quizresults"
