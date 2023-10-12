from django.db import models

# Create your models here.
# Temporär, nachher verschiebung in core


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.SmallIntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = "Benutzer"


class Question(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    flagged = models.BooleanField()
    _tags = models.TextField(db_column="tags")
    module = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()  # blank=True?

    class Meta:
        managed = False
        db_table = "Frage"

    @property
    def tags(self):
        return self._tags.split(",")
    
    @tags.setter
    def tags(self, tags_list):
        self._tags = ",".join(tags_list)
    

class Comment(models.Model):
    pass


class Answer(models.Model):
    pass
