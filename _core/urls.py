from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Root redirect

    # Apps
    path('account/', include(('_apps.account.urls', 'account'), namespace='account')),
    path('product/', include(('_apps.product.urls', 'product'), namespace='product')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
