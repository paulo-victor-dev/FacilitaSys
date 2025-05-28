from django.urls import path

from .views import ProductListView

app_name = 'product'

urlpatterns = [
    path('catalog/', ProductListView.as_view(), name='catalog')
]