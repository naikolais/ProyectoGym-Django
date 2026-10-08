from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('planes/', views.listar_planes, name='listar_planes'),
    path('planes/nuevo/', views.crear_plan, name='crear_plan'),
    path('planes/editar/<int:pk>/', views.editar_plan, name='editar_plan'),
    path('planes/eliminar/<int:pk>/', views.eliminar_plan, name='eliminar_plan'),
]