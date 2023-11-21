from django.contrib import admin
from Core.models import Benutzer, Frage, Antwort, Modul, Tag


# Register your models here.
admin.site.register(Benutzer)
admin.site.register(Frage)
admin.site.register(Antwort)
admin.site.register(Modul)
admin.site.register(Tag)
