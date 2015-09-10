from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll
from django.template import Context,loader

def index(request):
    #return HttpResponse("Hello,world You`re at the poll index.")
    latest_poll_list=Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))
    #output=','.join([v.question for v  in latest_poll_list])
    #return HttpResponse(output)

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)


# Create your views here.
