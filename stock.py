"""
productos.py
------------
Responsable: Estudiante 3 (rol: Responsable de stock)

Registro básico del catálogo de productos.
El control de cantidades disponibles se hace en stock.py.
Persistencia en datos/productos.json
"""

from modulos.almacenamiento import leer_json, escribir_json, generar_id

ARCHIVO = "productos.json"


def registrar_producto(nombre, precio, stock_inicial=0):
    """
    Registra un nuevo producto en el catálogo.

    Parametros:
        nombre (str): nombre del producto.
        precio (float): precio unitario.
        stock_inicial (int): cantidad inicial disponible.

    Retorna:
        dict: el producto creado, o None si los datos no son válidos.
    """
    if not nombre or not nombre.strip():
        print("Error: el nombre del producto no puede estar vacío.")
        return None
    if precio < 0:
        print("Error: el precio no puede ser negativo.")
        return None
    if stock_inicial < 0:
        print("Error: el stock inicial no puede ser negativo.")
        return None

    productos = leer_json(ARCHIVO)
    nuevo_producto = {
        "id": generar_id(productos, "id"),
        "nombre": nombre.strip(),
        "precio": precio,
        "stock": stock_inicial,
    }
    productos.append(nuevo_producto)
    escribir_json(ARCHIVO, productos)
    print(f"Producto registrado con id {nuevo_producto['id']}.")
    return nuevo_producto


def buscar_producto(producto_id):
    """
    Busca un producto por id. Retorna dict o None.
    """
    productos = leer_json(ARCHIVO)
    for producto in productos:
        if producto["id"] == producto_id:
            return producto
    return None


def listar_productos():
    """
    Retorna la lista completa de productos.
    """
    return leer_json(ARCHIVO)
