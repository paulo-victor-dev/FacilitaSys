from django.urls import path

from .views import *


app_name = 'account'

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('register/success/', RegisterSuccessView.as_view(), name='register_success'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogouView.as_view(), name='logout'),

    # Account activation
    path('activate/<uidb64>/<token>/', ActivationAccountView.as_view(), name="account_activate"),

    # Password reset
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]