from rest_framework import viewsets
from .models import Categoria, Producto, Cliente, Pedido
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, PedidoSerializer
import csv
from django.http import HttpResponse


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

def exportar_productos_csv(request):
    categoria_id = request.GET.get('categoria')
    estado = request.GET.get('estado')

    # Filtrar productos según los parámetros
    productos = Producto.objects.all()

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    if estado:
        productos = productos.filter(estado=estado)

    # Crear la respuesta como archivo CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="productos.csv"'

    # Crear un escritor de CSV
    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Categoría', 'Precio', 'Stock', 'Estado'])

    # Escribir los productos en el CSV
    for producto in productos:
        writer.writerow([
            producto.nombre,
            producto.categoria.nombre,  # Suponiendo que tienes una relación de clave foránea con Categoria
            producto.precio,
            producto.stock,
            producto.estado,
        ])

    return response