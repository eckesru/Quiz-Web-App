from django.contrib import admin
from Core.models import Benutzer, Frage, Modul, Tag, Antwort


# Register your models here.
admin.site.register(Benutzer)
admin.site.register(Frage)
admin.site.register(Modul)
admin.site.register(Tag)
admin.site.register(Antwort)
