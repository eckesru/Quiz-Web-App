from django.db import models
from django.contrib.auth.models import AbstractUser


class Benutzer(AbstractUser):
    _role = models.SmallIntegerField(default=0)
    _points = models.IntegerField(default=0)
    liked_fragen = models.ManyToManyField("Frage", blank=True)
    liked_antworten = models.ManyToManyField("Antwort", blank=True)
    study_area = models.ForeignKey("StudyArea",
                                   blank=False,
                                   on_delete=models.DO_NOTHING)

    @property
    def role(self):
        pass

    @role.setter
    def role(self, points):
        pass

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        raise AttributeError("Punkte dürfen nicht manuell gesetzt werden. \
                              Verwende statische calculate_points-Methode!")

    @staticmethod
    def update_points(user):
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
    flagged = models.BooleanField(default=0)
    tag = models.ManyToManyField(Tag)
    module = models.ForeignKey("Modul",
                               on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=0)

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
    flagged = models.BooleanField(default=0)
    text = models.TextField()
    likes = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = "Antwort"


class StudyArea(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "StudyArea"


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
    frage_mutiplier = 3
    antwort_multiplier = 1
    like_multiplier = 2

    # Berechnung der einzelnen Punkte anhand der Gewichte
    frage_points = fragen_amount * frage_mutiplier
    antwort_points = antworten_amount * antwort_multiplier
    like_points = likes_amount * like_multiplier

    # Gesamtsumme der Punkte als Ergebnis zurückgeben
    points = frage_points + antwort_points + like_points
    return points
