from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'api'

urlpatterns = [
    path('sendmail/', views.SendMailView.as_view()),
]