from django.urls import path

from .views import *

app_name = 'inventory'

urlpatterns = [
    path('flow_list/', FlowListView.as_view(), name='flow_list'),
]