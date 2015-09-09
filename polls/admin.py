from django.contrib import admin
from polls.models import Poll,Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
	#fields=['pub_date','question']
	fieldsets=[
		(None,{'fields':['question']}),
		('Date informantion',{'fields':['pub_date'],'classes':['collapse']}),
]
        list_display=('question','pub_date','was_published_recently')
	list_filter=['pub_date']
	search_fields=['question']
	date_hierarchy='pub_date'
	inlines=[ChoiceInline]

admin.site.register(Poll,PollAdmin)
#admin.site.register(Choice)
# Register your models here.

