from django.shortcuts import render
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.views.generic import CreateView
from django.views import View

from .forms import CustomUserCreationForm
from .models import User
from .tokens import CustomActivationToken


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('account:register_success')

    def form_valid(self, form):
        user = form.save()
        
        token_generator = CustomActivationToken()
        token = token_generator.make_token(user)

        uid = urlsafe_base64_encode(force_bytes(user.pk))

        activation_link = self.request.build_absolute_uri(
            reverse('account:account_activate', kwargs={'uidb64': uid, 'token': token})
        )

        send_mail(
            'Ative sua conta',
            f'Clique no link para ativar sua conta: {activation_link}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False
        )

        return super().form_valid(form)
    

class RegisterSuccessView(View):
    def get(self, request):
        return render(request, 'registration/register_success.html')
    

class ActivationAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            user = None

        token_generator = CustomActivationToken()

        if user is not None:
            if user.is_active:
                return render( 
                    request,
                    'registration/activation_invalid.html', 
                    {'id_msg': '1', 'message': 'Parece que sua conta já está ativa. Por favor, efetue o login.'}
                )

            elif token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                return render(request,'registration/activation_success.html')
    
        return render(request, 'registration/activation_invalid.html', {'id_msg': '2','message': 'Link de ativação inválido ou expirado. Clique abaixo para solicitar um novo link.'})


class ActivationInvalidView(View):
    def get(self, request):
        return render(request, 'registration/activation_invalid.html') 