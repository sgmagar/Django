from django.contrib import admin

# Register your models here.
from .models import Question, Answer_Choice, Score

class ChoiceInline(admin.TabularInline):
	model = Answer_Choice
	extra = 4

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text', 'position']
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
	]
	inlines = [ChoiceInline]

	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer_Choice)
admin.site.register(Score)

