from pprint import pprint
from collections import defaultdict
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.core import signing

from .models import Product, ProductVariant


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        query = Product.objects.filter(
            is_active=True, 
            variant_product__stock__gt=0
        ).distinct()

        return query.prefetch_related(
            Prefetch(
                'variant_product',
                queryset=ProductVariant.objects.filter(
                    is_active=True, 
                    stock__gt=0
                ).select_related('color', 'size').prefetch_related('variant_image'),
                to_attr='variants'
            )
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for product in context['products']:
            variant_data = defaultdict(dict)
            variants_stock = []

            for v in product.variants:
                color = v.color
                size = v.size
                variant_id = v.id
                stock = v.stock

                if color.id not in variant_data:
                    first_img = v.variant_image.all().first()
                    img_url = first_img.image.url if first_img else None

                    variant_data[color.id] = {
                        'color_name': color.name,
                        'image_url': img_url,
                        'sizes': []
                    }

                variant_data[color.id]['sizes'].append({
                    'size_id': size.id,
                    'size_name': size.name,
                    'variant_id': variant_id,
                    'stock': stock
                })
                variants_stock.append(stock)
            
            product.variant_data = variant_data

            product.signed_token = signing.dumps({
                'product_id': product.id,
                'colors_id': list(variant_data.keys()),
                'variants_stock': variants_stock
            }, salt='variant-data')

        return context

            #pprint(variant_data)
            
            # images = []
            
            # colors_ids = set()

            # for v in product.variants:
            #     color = v.color
            #     if color.id in colors_ids:
            #         continue

            #     first_img = v.variant_image.all().first()
            #     if first_img:
            #         images.append(first_img)
            #         colors_ids.add(color.id)

            #     data[v.color.name][v.size.name] = {
            #         'stock': v.stock,
            #         'variant_id': v.id,
            #     }
            #     variants_stock.append(v.stock)

            # product.variant_data = dict(data)
            # product.images = images

            # payload = {
            #     'product_id': product.id,
            #     'color_ids': list(colors_ids),
            #     'variants_stock': variants_stock
            # }

            # product.signed_token = signing.dumps(payload, salt='variant-data')
            # print(dict(data))

        

            # id_colors = set()
            # images = []

            # for variant in product.variants:
            #     color = variant.color
            #     if color.id in id_colors:
            #         continue

            #     first_img = variant.variant_image.all().first()
            #     if first_img:
            #         images.append(first_img)
            #         id_colors.add(color.id)

            # product.images = images

            # product.colors = list({
            #     v.color for v in product.variants
            # })

            # product.sizes = list({v.size for v in product.variants})

            # product.variant_stock = list({v.stock for v in product.variants})

            # payload = {
            #     'product_id': product.id,
            #     'color_ids': [c.id for c in product.colors],
            #     'size_ids': [s.id for s in product.sizes],
            #     'variant_stock_ids': [int(vs) for vs in product.variant_stock]
            # }

            # product.signed_token = signing.dumps(payload, salt='add-to-cart')
        

            
  
        
        
