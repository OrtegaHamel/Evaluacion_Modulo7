from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count, Avg
from .models import Producto, Categoria, Etiqueta, DetalleProducto, ProductoConEtiquetas
from .forms import ProductoForm, CategoriaForm, EtiquetaForm, DetalleProductoForm, RegistroForm

@login_required
def index(request):
    return render(request, 'productos/index.html')

def error_403(request, exception):
    return render(request, '403.html', status=403)

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)  # Usa el formulario personalizado
        if form.is_valid():
            user = form.save()  # Guarda el usuario y asigna el grupo
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

# --- Vistas para Productos ---
@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

@login_required
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle.html', {'producto': producto})

@login_required
@permission_required('productos.add_producto', raise_exception=True)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, 'Producto creado con éxito.')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear.html', {'form': form})

@login_required
@permission_required('productos.change_producto', raise_exception=True)
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado con éxito.')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar.html', {'form': form, 'producto': producto})

@login_required
@permission_required('productos.delete_producto', raise_exception=True)
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado con éxito.')
        return redirect('lista_productos')
    return render(request, 'productos/eliminar.html', {'producto': producto})

# --- Vistas para Categorías ---
@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista.html', {'categorias': categorias})

@login_required
@permission_required('productos.add_categoria', raise_exception=True)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada con éxito.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/formulario.html', {'form': form})

@login_required
@permission_required('productos.change_categoria', raise_exception=True)
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada con éxito.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/formulario.html', {'form': form})

@login_required
@permission_required('productos.delete_categoria', raise_exception=True)
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada con éxito.')
        return redirect('lista_categorias')
    return render(request, 'categorias/eliminar.html', {'categoria': categoria})

# --- Vistas para Etiquetas ---
@login_required
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'etiquetas/lista.html', {'etiquetas': etiquetas})

@login_required
@permission_required('productos.add_etiqueta', raise_exception=True)
def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta creada con éxito.')
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    return render(request, 'etiquetas/formulario.html', {'form': form})

@login_required
@permission_required('productos.change_etiqueta', raise_exception=True)
def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta actualizada con éxito.')
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'etiquetas/formulario.html', {'form': form})

@login_required
@permission_required('productos.delete_etiqueta', raise_exception=True)
def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        etiqueta.delete()
        messages.success(request, 'Etiqueta eliminada con éxito.')
        return redirect('lista_etiquetas')
    return render(request, 'etiquetas/eliminar.html', {'etiqueta': etiqueta})

@login_required
def consultas_orm(request):
    # Consulta 1: Todos los productos
    todos_productos = Producto.objects.all()
    # Consulta 2: Productos con nombre (interactivo)
    nombre_busqueda = request.GET.get('nombre_busqueda', '')
    productos_laptop = Producto.objects.filter(nombre__icontains=nombre_busqueda) if nombre_busqueda else Producto.objects.none()
    # Consulta 3: Productos de una categoría específica (interactivo)
    categoria_id = request.GET.get('categoria_id', '')
    productos_electronicos = Producto.objects.filter(categoria__id=categoria_id) if categoria_id else Producto.objects.none()
    # Consulta 4: Productos con precio mayor a un valor (interactivo)
    precio_minimo = request.GET.get('precio_minimo', 100)
    productos_caros = Producto.objects.filter(precio__gt=precio_minimo)
    # Consulta 5: Productos que no son de una categoría específica (interactivo)
    categoria_excluir_id = request.GET.get('categoria_excluir_id', '')
    productos_no_electronicos = Producto.objects.exclude(categoria__id=categoria_excluir_id) if categoria_excluir_id else Producto.objects.none()
    # Consulta 6: Número de productos por categoría
    categorias_con_conteo = Categoria.objects.annotate(num_productos=Count('productos'))
    # Consulta 7: Precio promedio por categoría
    categorias_con_promedio = Categoria.objects.annotate(precio_promedio=Avg('productos__precio'))
    # Consulta 8: Productos con una etiqueta específica (interactivo)
    etiqueta_id = request.GET.get('etiqueta_id', '')
    productos_oferta = Producto.objects.filter(etiquetas__id=etiqueta_id) if etiqueta_id else Producto.objects.none()
    # Consulta SQL personalizada: Productos con sus categorías y número de etiquetas
    query = """
    SELECT p.id, p.nombre, p.precio, c.nombre as categoria, COUNT(e.id) as num_etiquetas
    FROM productos_producto p
    LEFT JOIN productos_categoria c ON p.categoria_id = c.id
    LEFT JOIN productos_producto_etiquetas pe ON p.id = pe.producto_id
    LEFT JOIN productos_etiqueta e ON pe.etiqueta_id = e.id
    GROUP BY p.id, c.nombre
    """
    productos_con_etiquetas = ProductoConEtiquetas.objects.raw(query)
    # Obtener todas las categorías y etiquetas para los formularios
    categorias = Categoria.objects.all()
    etiquetas = Etiqueta.objects.all()
    return render(request, 'productos/consultas_orm.html', {
        'todos_productos': todos_productos,
        'productos_laptop': productos_laptop,
        'productos_electronicos': productos_electronicos,
        'productos_caros': productos_caros,
        'productos_no_electronicos': productos_no_electronicos,
        'categorias_con_conteo': categorias_con_conteo,
        'categorias_con_promedio': categorias_con_promedio,
        'productos_oferta': productos_oferta,
        'productos_con_etiquetas': productos_con_etiquetas,
        'categorias': categorias,
        'etiquetas': etiquetas,
        'nombre_busqueda': nombre_busqueda,
        'precio_minimo': precio_minimo,
    })
