from multiprocessing import context
from django.shortcuts import render
from django.views import generic
from .models import Workers


def home(request):
    if 'q' in request.GET:
        search_key = request.GET['q']
        workers = Workers.objects.filter(name__icontains=search_key)
    else:
        workers = Workers.objects.all()
        
    context = {
        "workers": workers
    }
    
    return render(request, 'pages/home.html', context)
