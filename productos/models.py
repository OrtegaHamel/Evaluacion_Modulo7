from django.db import models

# Modelo para Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para Etiqueta
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='productos')

    def __str__(self):
        return self.nombre

# Modelo para DetalleProducto
class DetalleProducto(models.Model):
    producto = models.OneToOneField('Producto', on_delete=models.CASCADE, related_name='detalles')
    dimensiones = models.CharField(max_length=100, blank=True, null=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        producto_nombre = self.producto.nombre if self.producto else "Sin producto"
        dimensiones = self.dimensiones if self.dimensiones else "Sin dimensiones"
        peso = self.peso if self.peso else "Sin peso"
        return f"Detalles de {producto_nombre}: {dimensiones}, {peso}"

# Modelo para consulta SQL personalizada
class ProductoConEtiquetas(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    num_etiquetas = models.IntegerField()

    class Meta:
        managed = False

