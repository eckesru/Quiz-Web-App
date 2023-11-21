from django.contrib import admin
from .models import *

class QuesModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'category')
    list_filter = ('category',)
    search_fields = ('question',)

class QuizCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(QuesModel, QuesModelAdmin)
admin.site.register(QuizCategory, QuizCategoryAdmin)
