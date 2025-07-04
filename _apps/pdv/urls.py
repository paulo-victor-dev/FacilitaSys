from django.urls import path

from .views import *

app_name = 'pdv'

urlpatterns = [
    path('', PdvView.as_view(), name='pdv'),
]
