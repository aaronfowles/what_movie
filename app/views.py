from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    # Get all known tags
<<<<<<< HEAD
    # Select 5 for questions
    return render(request, 'app/index.html', {"all_tags": "I don't know"})
=======
    all_tags = list(models.Tag.objects.all())
    # Select 5 for questions
    question_tags = list( all_tags[:5])
    context['all_tags'] = all_tags
    context['question_tags'] = question_tags
    return render(request, 'app/index.html', context)
>>>>>>> f00ef8906f2adae77317935bd723d85aab905ba8
