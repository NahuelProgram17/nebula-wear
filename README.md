# 🛍️ Nebula Wear

Nebula Wear es una aplicación web desarrollada con **Django** que simula una tienda online de ropa urbana/anime.  
El proyecto fue creado con fines educativos y de portfolio, enfocado en una estructura clara y funcionalidades reales de e-commerce.

---

## 🚀 Funcionalidades

- Listado de productos
- Filtrado por categorías (Remeras, Buzos, etc.)
- Vista de detalle de producto
- Carrito de compras simple
  - Agregar productos
  - Ver cantidades
  - Calcular subtotales y total
- Panel de administración con Django Admin

---

## 🧰 Tecnologías utilizadas

- Python 3.11
- Django 4.2
- HTML5
- CSS3
- JavaScript (básico)
- SQLite

---

## 📦 Instalación y ejecución

Clonar el repositorio:

```bash
git clone https://github.com/NahuelProgram17/nebula-wear.git
cd nebula-wear
Crear y activar entorno virtual:

python -m venv venv
Activar entorno virtual:

venv\Scripts\activate
Instalar dependencias:

pip install -r requirements.txt
Aplicar migraciones:

python manage.py migrate
Crear superusuario (opcional):

python manage.py createsuperuser
Ejecutar servidor:

python manage.py runserver
Abrir en el navegador:

http://127.0.0.1:8000/
🔐 Panel de administración
Acceso al admin de Django:

http://127.0.0.1:8000/admin/
Desde el panel se pueden:

Crear y editar productos

Administrar categorías

Ver carritos y productos agregados

📁 Estructura del proyecto
nebula/
│── backend/
│   ├── core/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   └── static/
│   ├── settings.py
│   └── urls.py
│── media/
│── requirements.txt
│── manage.py
📌 Notas
El carrito está implementado de forma simple con fines demostrativos.

No incluye pagos reales.

Proyecto pensado para portfolio y práctica con Django.

👤 Autor
Desarrollado por Nahuel Pedreyra
Proyecto de práctica y portfolio.
