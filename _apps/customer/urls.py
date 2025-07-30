from django.urls import path

from .views import *

app_name = 'customer'

urlpatterns = [
    # List
    path('customer_list/', CustomerListView.as_view(), name='customer_list'),

    # Export
    # path('user_list/export/', ExportUsersView.as_view(), name='user_list_export'),

    # CRUD
    path('customer_create/', CustomerCreateView.as_view(), name='customer_create'),
    # path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    # path('user_delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]