from django.db import models

# Modelo para Categoría (relación muchos a uno con Producto)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para Etiqueta (relación muchos a muchos con Producto)
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para DetalleProducto (relación uno a uno con Producto)
class DetalleProducto(models.Model):
    dimensiones = models.CharField(max_length=100, blank=True, null=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Detalles: {self.dimensiones}, {self.peso}"

# Modelo para Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='productos')
    detalles = models.OneToOneField(DetalleProducto, on_delete=models.CASCADE, blank=True, null=True, related_name='producto')

    def __str__(self):
        return self.nombre

