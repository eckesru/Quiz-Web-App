from django.contrib import admin
from Core.models import Benutzer, Frage, Antwort, Modul, Tag, StudyArea


# Register your models here.
admin.site.register(Benutzer)
admin.site.register(Frage)
admin.site.register(Antwort)
admin.site.register(Modul)
admin.site.register(Tag)


class StudyAreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register your models here.
admin.site.register(StudyArea, StudyAreaAdmin)
