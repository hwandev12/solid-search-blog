from django.views import generic


class BaseTemplateView(generic.TemplateView):
    template_name = 'pages/home.html'
