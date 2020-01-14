from django.contrib import admin
from .models import Question
from .models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields:'['pub_date', 'question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':
        ['collapse']}),
    ]
    inline = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
admin.site.register(Question, QuestionAdmin)