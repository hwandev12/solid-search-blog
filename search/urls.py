from django.urls import path
from .views import BaseTemplateView

app_name = 'blog'

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='home')
]
