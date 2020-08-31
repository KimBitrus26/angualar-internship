
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import  Question,  Story



#from .tools import can_add_question, can_modify, can_like, grade, token
from django.contrib.auth import authenticate, login, logout
from datetime import datetime 

# Create your views here.

def hello_world(request):
    return render(request, 'index.html', {})


def question(request):
    storys = Story.objects.all()
    questions = Question.objects.all()
    context = {
        "storys":storys,
        'questions':questions
        } 
    score = 0
    total = []
    
    for question in questions:
        if request.method == "POST":
            if question.id == 12:
                selected = request.POST["test"]
                if selected == question.answer:
                    score += 5
                total.append(score) 
                print(score)
                   
            elif question.id == 2:
                selected = request.POST["test"]
                if selected == question.answer:
                    score += 5
                    total.append(score) 
            elif question.id == 3:
                selected = request.POST["test"]
                if selected == question.answer:
                    score += 5
                    total.append(score)       
            elif question.id == 4:
                selected = request.POST["test"]
                if selected == question.answer:
                    score += 5
                    total.append(score) 
            elif question.id == 5:
                selected = request.POST["test"]
                if selected == question.answer:
                    score += 5
                    total.append(score) 
            elif question.id == 6:
                selected = request.POST["test"]
                if selected == question.answer:
                    score += 5
                    total.append(score) 
            elif question.id == 7:
                selected = request.POST["test"]
                if selected == question.answer:
                    score += 5
                    total.append(score) 
            elif question.id == 8:
                selected = request.POST["test"]
                if selected == question.answer:
                    score += 5
                    total.append(score) 
            elif question.id == 9:
                selected = request.POST["test"]
                if selected == question.answer:
                    score += 5
                    total.append(score) 
            elif question.id == 10:
                selected = request.POST["test"]
                if selected == question.answer:
                    score += 5
            total.append(score) 
            eligible_score = sum(total * 100) // 50
            if eligible_score >= 75:
                return redirect("eligble", {"eligible_score":eligible_score})
                print(eligible_score)
            else:
                return render(request, "non_eligible.html", {"eligible_score":eligible_score})

    return render(request, "question.html", context )
    
   
def eligble(request):
    return render(request, "eligible.html")

def non_eligble(request):
    return render(request, "non_eligible.html")
