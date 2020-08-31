from django.db import models

# Create your models here.

class Story(models.Model):
    story_body = models.TextField(help_text="Input text", blank=True)
    
    def __str__(self):
        return self.story_body

class Question(models.Model):
    #story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="story", null=True)
    question_body = models.CharField(max_length=800, help_text="Input a question", blank=True)
    option1 = models.CharField(max_length=800, help_text="Input option 1", blank=True)
    option2 = models.CharField(max_length=800, help_text="Input option 2", blank=True)
    option3 = models.CharField(max_length=800, help_text="Input option 3", blank=True)
    option4 = models.CharField(max_length=800, help_text="Input option 4", blank=True)
    answer = models.CharField(max_length=800, help_text="Input option answere", blank=True)
    
    def __str__(self):
        return self.question_body
