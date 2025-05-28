from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from .views import RegisterView, RegisterSuccessView, ActivationAccountView, ActivationInvalidView
from .forms import CustomPasswordResetForm, CustomLoginForm


app_name = 'account'

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),

    path('login/', auth_views.LoginView.as_view(
        authentication_form = CustomLoginForm,
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Account activation
    path('register/success', RegisterSuccessView.as_view(), name='register_success'),
    path('activate/<uidb64>/<token>', ActivationAccountView.as_view(), name="account_activate"),
    path('activate/invalid', ActivationInvalidView.as_view(), name="activate_invalid"),

    # Password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(
        form_class = CustomPasswordResetForm,
        success_url=reverse_lazy('account:password_reset_done')
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url = reverse_lazy("account:password_reset_complete")
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]