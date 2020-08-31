from django.contrib import admin
from . models import Question, Story

# Register your models here.




class QuestionAdmin(admin.ModelAdmin):

    pass


class StoryAdmin(admin.ModelAdmin):

    pass

admin.site.register(Question, QuestionAdmin)

admin.site.register(Story, StoryAdmin)


