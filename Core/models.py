from django.db import models
from django.contrib.auth.models import AbstractUser


class Benutzer(AbstractUser):
    _role = models.SmallIntegerField(default=0)
    points = models.IntegerField(default=0)

    @property
    def role(self):
        pass

    @role.setter
    def role(self, points):
        pass

    class Meta:
        managed = False
        db_table = "Benutzer"


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
    _tags = models.TextField(db_column="tags")
    module = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __init__(self, user, _tags, module, title, text):
        super().__init__()
        self.user = user
        self.tags = _tags
        self.module = module
        self.title = title
        self.text = text

    class Meta:
        managed = False
        db_table = "Frage"

    @property
    def tags(self):
        return self._tags.split(",")

    @tags.setter
    def tags(self, tags_list):
        self._tags = ",".join(tags_list)


class Kommentar(models.Model):
    pass

    class Meta:
        managed = False
        db_table = "Kommentar"


class Antwort(models.Model):
    pass


    class Meta:
        managed = False
        db_table = "Antwort"
