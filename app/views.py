from django.shortcuts import render
from . import models
from random import randint

# Create your views here.
def index(request):
    context = {}
    # Get all known tags
    # Select 5 for questions
    all_tags = list(models.Tag.objects.all())
    # Select 5 for questions
    rand_selection = []
    for i in range(0,5):
        rand_selection.append(randint(0,len(all_tags)-1))
    context['question_tags'] = []
    for i in range(0,5):
        context['question_tags'].append(all_tags[rand_selection[i]])
    return render(request, 'app/index.html', context)
