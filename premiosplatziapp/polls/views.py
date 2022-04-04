from django.shortcuts import get_object_or_404, render,get_list_or_404
from django.http import HttpRequest, HttpResponse
from .models import Question
# Create your views here.
def index(request):
    lasted_question_list=Question.objects.all()
    return render(request,"polls/index.html",{
        "lasted_question_list":lasted_question_list
    })
    #HttpResponse("Estas en la pagina principal")

def detail(request,question_id):
    question=get_object_or_404(Question, pk=question_id)
    return   render(request,"polls/detail.html",{
        "question":question
    })
    #HttpResponse(f"Estas viendo la pregunta numero {question_id}")


def results(request,question_id):
    return HttpResponse(f"Estas viendo los resultados la pregunta numero {question_id}")



def vote(request,question_id):
    return HttpResponse(f"Estas votando a la pregunta numero {question_id}")
