from django.urls import path

from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('overview/', DashboardView.as_view(), name='overview'),
]