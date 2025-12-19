from django.urls import path, include

urlpatterns = [
    # Auth urls
    path("", include("apps.authentication.urls")),
    
    # Apps urls
    path("", include("apps.supplier.urls")),
    
]