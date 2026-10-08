from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('planes.urls')),  # Redirige la ruta principal a la app 'planes'
]