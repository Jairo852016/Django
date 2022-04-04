from importlib.resources import contents
from re import template
from django.shortcuts import get_object_or_404, render,get_list_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choise
# Create your views here.
#def index(request):
#    latest_question_list=Question.objects.all()
#    return render(request,"polls/index.html",{
#       "latest_question_list":latest_question_list
#    })
    #HttpResponse("Estas en la pagina principal")

#def detail(request,question_id):
#    question=get_object_or_404(Question, pk=question_id)
#    return   render(request,"polls/detail.html",{
#        "question":question
#    })
    #HttpResponse(f"Estas viendo la pregunta numero {question_id}")


#def results(request,question_id):
#    question= get_object_or_404(Question, pk=question_id)
#
#    return  render(request, "polls/results.html",{
#        "question":question
#    })

class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name= "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detail.html"

class ResultView(generic.DetailView):
    model=Question
    template_name="polls/results.html" 
    

    



def vote(request,question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choise_set.get(pk=request.POST["choice"])
    except(KeyError,Choise.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question":question,
            "error_message":"No elegiste una respuesta"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



    ###return HttpResponse(f"Estas votando a la pregunta numero {question_id}")
