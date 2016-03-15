from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    context = {}
    # Get all known tags
    all_tags = models.Tag.objects.all()
    # Select 5 for questions
    question_tags = all_tags[:5]
    context['all_tags'] = all_tags
    context['question_tags'] = question_tags
    return render(request, 'app/index.html', context)
