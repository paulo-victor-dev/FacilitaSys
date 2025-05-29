from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import product


class ProductListView(LoginRequiredMixin, ListView):
    model = product.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
        

            
  
        
        
