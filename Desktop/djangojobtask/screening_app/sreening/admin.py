from django.contrib import admin
from . models import Question, Story
from django.contrib.auth.models import User
# Register your models here.




class QuestionAdmin(admin.ModelAdmin):

    pass


class StoryAdmin(admin.ModelAdmin):

    pass

class UserAdmin(admin.ModelAdmin):

    pass


admin.site.register(Question, QuestionAdmin)

admin.site.register(Story, StoryAdmin)
admin.site.register(User, UserAdmin)

