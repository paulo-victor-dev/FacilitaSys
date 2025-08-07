from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render

from _apps.order.models import Order

class PdvView(LoginRequiredMixin, View):
    def get(self, request):
        last_order = Order.objects.last()

        if last_order:
            next_order = last_order.id + 1 
        else:
            next_order = 1
            

        context = {
            'next_order': next_order,

        }

        return render(request, 'partials/_pdv.html', context)
    

