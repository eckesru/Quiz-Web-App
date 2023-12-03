from django.db import models
from django.contrib.auth.models import AbstractUser


class Benutzer(AbstractUser):
    _points = models.IntegerField(default=0)
    _rank = models.CharField(max_length=255)
    liked_fragen = models.ManyToManyField("Frage", blank=True)
    liked_antworten = models.ManyToManyField("Antwort", blank=True)
    study_area = models.ForeignKey("StudyArea",
                                   blank=False,
                                   on_delete=models.DO_NOTHING)
    answered_frage_des_tages = \
        models.ManyToManyField('Quiz.QuesModel', through='BenutzerQuesModel')

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        raise AttributeError("Punkte dürfen nicht manuell gesetzt werden. \
                              Verwende update_points_for_user()-Methode!")

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        raise AttributeError("Ränge dürfen nicht manuell gesetzt werden. \
                              Verwende update_points_for_user()-Methode!")

    @staticmethod
    def update_points(user):
        from .utils import update_points_for_user
        update_points_for_user(user)

    class Meta:
        managed = False
        db_table = "Benutzer"


class Tag(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    str_id = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = "Tag"


class Modul(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    str_id = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = "Modul"


class Frage(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey("Benutzer",
                             on_delete=models.DO_NOTHING)
    # on_delete=models.CASCADE -> PlanetBase unterstützt keine Constraints
    # bzw. referenzielle Integrität aufgrund Performancefokus
    # db_constraint=False -> Falls Migrationsprobleme, wieder reinnehmen
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)
    module = models.ForeignKey("Modul",
                               on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = "Frage"

#    @property
#    def tags(self):
#        return self._tags.split(",")

#    @tags.setter
#    def tags(self, tags_list):
#        self._tags = ",".join(tags_list)


""" class Kommentar(models.Model):
    pass

    class Meta:
        managed = False
        db_table = "Kommentar" """


class Antwort(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey("Benutzer",
                             on_delete=models.DO_NOTHING)
    frage = models.ForeignKey("Frage",
                              on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    text = models.TextField()
    likes = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = "Antwort"


class StudyArea(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    shortname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "StudyArea"


class BenutzerQuesModel(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey('Benutzer', on_delete=models.DO_NOTHING)
    quizfrage = models.ForeignKey('Quiz.QuesModel',
                                  on_delete=models.DO_NOTHING)
    answer = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "Benutzer_Quesmodel"
