from django.urls import path

from .views import *


app_name = 'account'

urlpatterns = [
    # Authentication
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogouView.as_view(), name='logout'),

    # Password reset
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]