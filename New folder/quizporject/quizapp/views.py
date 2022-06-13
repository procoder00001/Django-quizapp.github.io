from contextvars import Context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import QuizModel

from .forms import *

# Create your views here.

def home(request):
    if request.method =="POST":
        questions = QuizModel.objects.all()
        context = {'questions':questions}
        return render(request,"home/home.html",context)


def addquestion(request):
    form = addQuestionform()
    if request.method =="POST":
        form = addQuestionform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/addquestion")

    context = {'form':form}
    return render(request,'quizapp/AddQuestion.html',context)


def result(request):
    if request.method =="POST":
        questions = QuizModel.objects.all()
        score =0
        wrong =0
        correct =0
        total =0
        for q in questions:
            total =total+1
            if q.ans ==request.POST.get('q.question'):
                score =score+1
                correct =correct+1
            else:
                wrong =wrong +1

        

        context ={
            'score':f'{score}/{total}',
            'correct':correct,
            'wrong':wrong,
            'total':total,
        }
        return render(request,'quizapp/result.html',context)
    