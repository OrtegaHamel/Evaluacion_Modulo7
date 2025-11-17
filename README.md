# Gestión de Productos

Por Álvaro Ortega Hamel

Aplicación web desarrollada en **Django** para administrar productos,
categorías y etiquetas de forma eficiente. Incluye control de permisos,
autenticación y roles preconfigurados.

------------------------------------------------------------------------

## 📋 Requisitos Previos

-   Python 3.8+
-   Pip
-   Virtualenv (opcional)

------------------------------------------------------------------------

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio

``` bash
git clone <URL_DEL_REPOSITORIO>
cd M7_Evaluacion_Modulo
```

### 2. Crear y activar un entorno virtual

``` bash
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate   # Windows
```

### 3. Instalar dependencias

``` bash
pip install -r requirements.txt
```

Si no existe *requirements.txt*:

``` bash
pip install django gunicorn
```

### 4. Migrar la base de datos

``` bash
python manage.py migrate
```

### 5. Ejecutar el servidor

``` bash
python manage.py runserver
```

### 6. Acceder a la aplicación

http://127.0.0.1:8000/

------------------------------------------------------------------------

## 👤 Usuarios Preconfigurados

  Usuario           Contraseña      Grupo               Permisos
  ----------------- --------------- ------------------- ---------------
  root              root            Superusuario        Acceso total
  administrador     contrasena123   Editores            CRUD completo
  usuario_normal1   contrasena123   Usuarios normales   Solo lectura

------------------------------------------------------------------------

## 🧩 Permisos del Sistema

-   **Usuarios normales:** lectura de productos, categorías y
    etiquetas.\
-   **Editores:** CRUD completo.\
-   **Superusuario:** acceso total.\
-   Nuevos usuarios se asignan automáticamente al grupo *Usuarios
    normales*.

------------------------------------------------------------------------

## 📂 Estructura del Proyecto

    M7_Evaluacion_Modulo/
    ├── gestion_productos/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── productos/
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── 403.html
    │   │   ├── productos/
    │   │   ├── categorias/
    │   │   ├── etiquetas/
    │   │   └── registration/
    │   ├── models.py
    │   ├── views.py
    │   ├── forms.py
    │   ├── admin.py
    │   ├── urls.py
    │   └── migrations/
    ├── manage.py
    └── README.md

------------------------------------------------------------------------

## 📜 Licencia

Proyecto académico desarrollado para fines formativos.