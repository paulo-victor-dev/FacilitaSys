from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'partials/pages/dashboard.html'
 