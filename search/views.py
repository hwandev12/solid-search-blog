from django.views import generic
from .models import Workers

class BaseTemplateView(generic.ListView):
    template_name = 'pages/home.html'
    queryset = Workers.objects.all()
    context_object_name = 'workers'
