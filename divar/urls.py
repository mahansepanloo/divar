

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('prodact.urls')),
    path("accounts/", include('accounts.urls')),
    path('orders/', include('orders.urls')),
]
