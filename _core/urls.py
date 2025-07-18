from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Root redirect
    path('', RedirectView.as_view(url='dashboard/overview/'), name='root_redirect'),

    # Apps
    path('account/', include(('_apps.account.urls', 'account'), namespace='account')),

    path('product/', include(('_apps.product.urls', 'product'), namespace='product')),

    path('dashboard/', include(('_apps.dashboard.urls', 'dashboard'), namespace='dashboard')),

    path('order/', include(('_apps.order.urls', 'order'), namespace='order')),

    path('supplier/', include(('_apps.supplier.urls', 'supplier'), namespace='supplier')),
    
    path('stock/', include(('_apps.stock.urls', 'stock'), namespace='stock')),

    path('pdv/', include(('_apps.pdv.urls', 'pdv'), namespace='pdv')),

    path('customer/', include(('_apps.customer.urls', 'customer'), namespace='customer')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
