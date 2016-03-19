from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    # Get all known tags
    # Select 5 for questions
    return render(request, 'app/index.html', {"all_tags": "I don't know"})
