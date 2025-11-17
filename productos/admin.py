from django.contrib import admin
from .models import Producto, Categoria, Etiqueta, DetalleProducto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(DetalleProducto)
class DetalleProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'dimensiones', 'peso')
    search_fields = ('producto__nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('etiquetas',)  # Para una mejor gestión de relaciones muchos a muchos


