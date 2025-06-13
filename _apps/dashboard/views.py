from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from .forms import DatePeriodForm


class DashboardView(LoginRequiredMixin, FormView):
    template_name = 'dashboard.html'
    form_class = DatePeriodForm