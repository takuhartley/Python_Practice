from django.contrib import admin
from .models import Question
from .models import Choice
import datetime
import timezone

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
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(day=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
admin.site.register(Question, QuestionAdmin)