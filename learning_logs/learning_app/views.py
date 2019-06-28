from django.shortcuts import render

# Create your views here.
from .models import Topic


def index(request):
    return render(request, 'learning_app/base.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_app/topics.html', context)
