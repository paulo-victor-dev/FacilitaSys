from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models import Sum

from .models import Flow


class FlowListView(LoginRequiredMixin, ListView):
    model = Flow
    template_name = 'flow_list.html'
    context_object_name = 'flows'

   

    

