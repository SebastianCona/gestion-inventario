from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet, ClienteViewSet, PedidoViewSet
from .views import exportar_productos_csv

# Configuración del router para las vistas basadas en ViewSets
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)

# Combina las rutas del router con la ruta manual para exportar
urlpatterns = router.urls  # Estas son las rutas generadas por el DefaultRouter

# Añadir la ruta manual para exportar productos
urlpatterns = [
    path('productos/exportar/', exportar_productos_csv, name='exportar_productos'),
]
