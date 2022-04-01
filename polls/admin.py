from django.contrib import admin
from .models import Choice, Question
from .models import user

admin.site.register(Choice)
admin.site.register(user)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)