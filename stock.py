"""
stock.py
--------
Responsable: Estudiante 3 (rol: Responsable de stock)

Funciones:
    verificar_stock(producto_id, cantidad)
    agregar_stock(producto_id, cantidad)
    descontar_stock(producto_id, cantidad)
    mostrar_stock_bajo(minimo)

Persistencia en datos/productos.json (campo "stock" de cada producto).
"""

from modulos.almacenamiento import leer_json, escribir_json
from modulos.productos import ARCHIVO, buscar_producto


def verificar_stock(producto_id, cantidad):
    """
    Verifica si hay stock suficiente de un producto.

    Parametros:
        producto_id (int): id del producto.
        cantidad (int): cantidad solicitada.

    Retorna:
        True si hay stock suficiente, False si no o si el producto no existe.
    """
    producto = buscar_producto(producto_id)
    if producto is None:
        print(f"Error: el producto {producto_id} no existe.")
        return False
    if cantidad <= 0:
        print("Error: la cantidad debe ser mayor a 0.")
        return False
    return producto["stock"] >= cantidad


def agregar_stock(producto_id, cantidad):
    """
    Aumenta el stock disponible de un producto.

    Retorna:
        True si se agregó correctamente, False si hubo un error.
    """
    if cantidad <= 0:
        print("Error: la cantidad a agregar debe ser mayor a 0.")
        return False

    productos = leer_json(ARCHIVO)
    for producto in productos:
        if producto["id"] == producto_id:
            producto["stock"] += cantidad
            escribir_json(ARCHIVO, productos)
            print(f"Stock actualizado. Nuevo stock de '{producto['nombre']}': {producto['stock']}.")
            return True

    print(f"Error: el producto {producto_id} no existe.")
    return False


def descontar_stock(producto_id, cantidad):
    """
    Descuenta stock de un producto, validando disponibilidad previa.

    Retorna:
        True si se descontó correctamente, False si no hay stock suficiente
        o si el producto no existe.
    """
    if not verificar_stock(producto_id, cantidad):
        print("Error: no hay stock suficiente para descontar.")
        return False

    productos = leer_json(ARCHIVO)
    for producto in productos:
        if producto["id"] == producto_id:
            producto["stock"] -= cantidad
            escribir_json(ARCHIVO, productos)
            print(f"Stock descontado. Nuevo stock de '{producto['nombre']}': {producto['stock']}.")
            return True
    return False


def mostrar_stock_bajo(minimo):
    """
    Retorna la lista de productos cuyo stock es menor o igual al mínimo indicado.
    Útil para alertar antes de que un pedido no pueda despacharse.
    """
    productos = leer_json(ARCHIVO)
    return [p for p in productos if p["stock"] <= minimo]
