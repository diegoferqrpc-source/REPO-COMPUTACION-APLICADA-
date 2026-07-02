"""
despacho.py
-----------
Responsable: Estudiante 4 (rol: Responsable de despacho)

Funciones:
    asignar_despacho(codigo_pedido, repartidor)
    actualizar_estado(codigo_pedido, nuevo_estado)
    registrar_motivo_no_entrega(codigo_pedido, motivo)
    registrar_entrega(codigo_pedido)

Reutiliza pedidos.py para no duplicar la lógica de lectura/escritura de pedidos.
"""

from modulos.pedidos import ARCHIVO, ESTADOS_VALIDOS, buscar_pedido, cambiar_estado_pedido
from modulos.almacenamiento import leer_json, escribir_json


def asignar_despacho(codigo_pedido, repartidor):
    """
    Asigna un repartidor a un pedido y cambia su estado a 'en_ruta'.

    Retorna:
        True si se asignó correctamente, False si el pedido no existe
        o el nombre del repartidor está vacío.
    """
    if not repartidor or not repartidor.strip():
        print("Error: debe indicar el nombre del repartidor.")
        return False

    pedido = buscar_pedido(codigo_pedido)
    if pedido is None:
        print(f"Error: el pedido {codigo_pedido} no existe.")
        return False

    pedidos = leer_json(ARCHIVO)
    for p in pedidos:
        if p["codigo"] == codigo_pedido:
            p["repartidor"] = repartidor.strip()
            p["estado"] = "en_ruta"
            escribir_json(ARCHIVO, pedidos)
            print(f"Pedido {codigo_pedido} asignado a '{repartidor}' y marcado 'en_ruta'.")
            return True
    return False


def actualizar_estado(codigo_pedido, nuevo_estado):
    """
    Actualiza el estado de un pedido (pendiente, en_ruta, entregado,
    retrasado, no_entregado). Delegado en pedidos.cambiar_estado_pedido
    para mantener una sola fuente de verdad sobre los estados válidos.
    """
    return cambiar_estado_pedido(codigo_pedido, nuevo_estado)


def registrar_motivo_no_entrega(codigo_pedido, motivo):
    """
    Registra el motivo por el cual un pedido no fue entregado
    y cambia su estado a 'no_entregado'.

    Retorna:
        True si se registró correctamente, False en caso de error.
    """
    if not motivo or not motivo.strip():
        print("Error: debe indicar un motivo de no entrega.")
        return False

    pedido = buscar_pedido(codigo_pedido)
    if pedido is None:
        print(f"Error: el pedido {codigo_pedido} no existe.")
        return False

    pedidos = leer_json(ARCHIVO)
    for p in pedidos:
        if p["codigo"] == codigo_pedido:
            p["motivo_no_entrega"] = motivo.strip()
            p["estado"] = "no_entregado"
            escribir_json(ARCHIVO, pedidos)
            print(f"Pedido {codigo_pedido} marcado como 'no_entregado'. Motivo: {motivo}.")
            return True
    return False


def registrar_entrega(codigo_pedido):
    """
    Marca un pedido como entregado exitosamente.

    Retorna:
        True si se registró la entrega, False si el pedido no existe.
    """
    return cambiar_estado_pedido(codigo_pedido, "entregado")
