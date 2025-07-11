from django.urls import path

from .views import *

app_name = 'account'

urlpatterns = [
    # Authentication
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # List
    path('user_list/', UserListView.as_view(), name='user_list'),

    # Export
    path('user_list/export/', ExportUsersView.as_view(), name='user_list_export'),

    # CRUD
    path('user_create/', UserCreateView.as_view(), name='user_create'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user_delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]