from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tiendaApp.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('contact.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('accounts.urls')),
]
