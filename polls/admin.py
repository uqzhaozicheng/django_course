from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.site_index_title = 'Welcome to the Pollster admin area'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Information',{'fields':['question_text']}),
                 ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),]
    #collapse --> show or hid function
    
    inlines = [ChoiceInline]


#admin.site.register(Question)
#admin.site.register(Choice)  
admin.site.register(Question, QuestionAdmin)
