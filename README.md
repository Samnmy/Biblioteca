# 📚 Library Management System in Python

Este proyecto es un sistema básico de gestión de libros en Python, pensado para funcionar a través de una interfaz de consola. Permite registrar, buscar, actualizar, eliminar libros y generar reportes estadísticos de una biblioteca.

---

## 🧠 Características

- 📖 Registro de nuevos libros con validación de datos
- 🔍 Búsqueda de libros por título (insensible a mayúsculas/minúsculas)
- ✏️ Actualización de cantidad y precio de libros existentes
- 🗑️ Eliminación de libros por título
- 📊 Reporte de:
  - Libro más antiguo y más reciente
  - Valor total del inventario de libros

---

## 💾 Estructura de los libros

Cada libro es representado como un diccionario con los siguientes campos:

```python
{
    "title": "string",
    "author": "string",
    "year": int,
    "quantity": int,
    "price": float
}
