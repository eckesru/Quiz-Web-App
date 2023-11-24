from django.contrib import admin
from .models import QuesModel
from Core.models import StudyArea


class QuesModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'category')
    list_filter = ('category',)
    search_fields = ('question',)


# Register your models here.
admin.site.register(QuesModel, QuesModelAdmin)
