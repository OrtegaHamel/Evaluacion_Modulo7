# Gestión de Productos

### Ejercicio M7_Evaluacion_Modulo del Bootcamp FullStack Python  

Por Álvaro Ortega Hamel

Aplicación web desarrollada en **Django** para administrar productos,
categorías y etiquetas de forma eficiente. Incluye control de permisos,
autenticación y roles preconfigurados.

------------------------------------------------------------------------

## ¿Qué incluye este proyecto?

-   Sistema de productos, categorías y etiquetas
-   Gestión de permisos con grupos: usuarios normales, editores y superusuario
-   Templates reutilizables y manejo de errores
-   Migraciones y configuración completa del proyecto
-   Entorno virtual, dependencias y estructura ordenada

## Lo que aprendí:
Este proyecto fue clave para reforzar conceptos como arquitectura de proyectos Django y PostgreSQL, buenas prácticas de organización en backend, seguridad mediante permisos, y la importancia de documentar de forma clara para que otros (y uno mismo en el futuro) puedan entender y ejecutar el proyecto sin problemas.

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

| Usuario            | Contraseña     | Grupo               | Permisos                                                                 |
|--------------------|-----------------|---------------------|--------------------------------------------------------------------------|
| root               | root            | Superusuario        | Todos los permisos                                                     |
| administrador      | contrasena123  | Editores           | Permisos completos (CRUD) para Productos, Categorías y Etiquetas        |
| usuario_normal1    | contrasena123  | Usuarios normales  | Solo puede ver listas de Productos, Categorías y Etiquetas             |


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
    ├── img/
    ├── manage.py
    ├── Capturas.md    
    └── README.md

------------------------------------------------------------------------

## 📜 Licencia

Proyecto académico desarrollado para fines formativos.