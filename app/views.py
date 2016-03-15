from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    context = {}
    return render(request, 'app/index.html', context)
