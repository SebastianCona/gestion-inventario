from django.contrib import admin
from .models import Producto, Categoria, Cliente, Pedido


admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Pedido)
