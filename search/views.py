from django.views import generic


class BaseTemplateView(generic.TemplateView):
    template_name = 'layouts/base.html'
