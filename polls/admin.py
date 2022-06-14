from django.contrib import admin
from . import models

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text',)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text',)
    QuestionAdmin.list_display = ('question_text',)


admin.site.register(models.Choice, ChoiceAdmin)
admin.site.register(models.Question, QuestionAdmin)