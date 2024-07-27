from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

app_name = "admins"
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
