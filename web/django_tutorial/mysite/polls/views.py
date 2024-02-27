from django.http import HttpResponse  #, Http404
from django.template import loader
from django.shortcuts import get_object_or_404,render

from .models import Question

# Create your views here.
def index(request):
    #1
    #return HttpResponse("Hello, World")

    #2
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    #3
    #template = loader.get_template('polls/index.html')
    #context = {
    #    'latest_question_list' : latest_question_list,
    #}

    #4
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }    
    return render(request, 'polls/index.html',context)

def detail(request, question_id):
    # 1
    #return HttpResponse("You're looking at question %s." %question_id)

    #2
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exitst!!!")
    #return render(request, 'polls/detail.html',{'question' : question})

    #3
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html' , {'question' : question})

def results(request, question_id):
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voing on question %s."%question_id)
