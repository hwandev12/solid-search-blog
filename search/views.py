from django.shortcuts import render
from django.views import generic
from .models import Workers
from django.db.models import Q


def home(request):
    # In this method we can search anything related to following
    # We have used Q from imports
    # we have used something__icontains to search related to something
    # we have used filter method and request method as following
    if 'q' in request.GET:
        search_key = request.GET['q']
        full_search = Q(Q(name__icontains=search_key) | Q(last_name__icontains=search_key) | Q(profession__icontains=search_key))
        workers = Workers.objects.filter(full_search)
    else:
        workers = Workers.objects.all()
        
    context = {
        "workers": workers
    }
    
    return render(request, 'pages/home.html', context)
