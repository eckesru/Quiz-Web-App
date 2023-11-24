from django.db import models
from django.contrib.auth.models import AbstractUser
from utils import update_points_for_user


class Benutzer(AbstractUser):
    _role = models.SmallIntegerField(default=0)
    _points = models.IntegerField(default=0)
    liked_fragen = models.ManyToManyField("Frage", blank=True)
    liked_antworten = models.ManyToManyField("Antwort", blank=True)

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
