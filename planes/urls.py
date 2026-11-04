from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'api/planes', views.PlanEntrenamientoViewSet)

urlpatterns = [
    # Rutas web del CRUD y públicas
    path('', views.inicio, name='inicio'),
    path('planes/', views.listar_planes, name='listar_planes'),
    path('planes/nuevo/', views.crear_plan, name='crear_plan'),
    path('planes/editar/<int:pk>/', views.editar_plan, name='editar_plan'),
    path('planes/eliminar/<int:pk>/', views.eliminar_plan, name='eliminar_plan'),

    # Rutas de Autenticación Web (Login y Logout)
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Rutas de la API REST y generación de Token
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('generar-token/', views.vista_obtener_token, name='vista_obtener_token'),
]