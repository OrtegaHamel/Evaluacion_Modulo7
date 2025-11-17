from django import forms
from .models import Producto, Categoria, Etiqueta, DetalleProducto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']

class DetalleProductoForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = ['dimensiones', 'peso']

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Asignar al grupo "Usuarios normales"
            grupo_usuario_normal, created = Group.objects.get_or_create(name='Usuarios normales')
            user.groups.add(grupo_usuario_normal)
        return user