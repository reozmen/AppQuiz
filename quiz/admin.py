from django.contrib import admin
from .models import *
import nested_admin

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4

class QuestionInline(nested_admin.NestedTabularInline):
    inlines=[AnswerInline]
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerInline]


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines=[QuestionInline]
    extra = 1
    list_display = ('title',)
    ordering = ('title',)
    search_fields = ('title',)
    list_per_page = 10




admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
