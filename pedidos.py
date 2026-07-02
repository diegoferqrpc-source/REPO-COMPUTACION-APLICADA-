"""
pedidos.py
----------
Responsable: Estudiante 2 (rol: Responsable de pedidos)

Funciones:
    registrar_pedido(cliente_id, lista_productos)
    buscar_pedido(codigo)
    listar_pedidos()
    validar_datos_pedido(cliente_id, lista_productos)
    listar_pedidos_pendientes()

Estados posibles del pedido: pendiente, en_ruta, entregado, retrasado, no_entregado
Persistencia en datos/pedidos.json
"""

from datetime import date

from modulos.almacenamiento import leer_json, escribir_json, generar_id
from modulos.clientes import existe_cliente
from modulos.stock import verificar_stock, descontar_stock

ARCHIVO = "pedidos.json"

ESTADOS_VALIDOS = ["pendiente", "en_ruta", "entregado", "retrasado", "no_entregado"]


def validar_datos_pedido(cliente_id, lista_productos):
    """
    Valida que el cliente exista, que haya al menos un producto
    y que haya stock suficiente para cada producto solicitado.

    lista_productos: lista de dicts como
        [{"producto_id": 1, "cantidad": 2}, {"producto_id": 3, "cantidad": 1}]

    Retorna:
        True si los datos son válidos, False si no.
    """
    if not existe_cliente(cliente_id):
        print(f"Error: el cliente {cliente_id} no existe.")
        return False

    if not lista_productos:
        print("Error: el pedido debe tener al menos un producto.")
        return False

    for item in lista_productos:
        if "producto_id" not in item or "cantidad" not in item:
            print("Error: cada producto debe tener 'producto_id' y 'cantidad'.")
            return False
        if not verificar_stock(item["producto_id"], item["cantidad"]):
            print(f"Error: stock insuficiente para el producto {item['producto_id']}.")
            return False

    return True


def registrar_pedido(cliente_id, lista_productos, fecha=None):
    """
    Registra un nuevo pedido si los datos son válidos y descuenta el stock
    correspondiente a cada producto.

    Parametros:
        cliente_id (int): id del cliente.
        lista_productos (list): lista de {"producto_id": int, "cantidad": int}.
        fecha (str): fecha del pedido en formato YYYY-MM-DD. Si no se indica,
                     se usa la fecha actual.

    Retorna:
        dict: el pedido creado, o None si la validación falla.
    """
    if not validar_datos_pedido(cliente_id, lista_productos):
        return None

    # Descontar stock de cada producto (ya validado que hay disponibilidad)
    for item in lista_productos:
        descontar_stock(item["producto_id"], item["cantidad"])

    pedidos = leer_json(ARCHIVO)
    nuevo_pedido = {
        "codigo": generar_id(pedidos, "codigo"),
        "cliente_id": cliente_id,
        "productos": lista_productos,
        "fecha": fecha if fecha else str(date.today()),
        "estado": "pendiente",
        "repartidor": None,
        "motivo_no_entrega": None,
    }
    pedidos.append(nuevo_pedido)
    escribir_json(ARCHIVO, pedidos)
    print(f"Pedido registrado con código {nuevo_pedido['codigo']}.")
    return nuevo_pedido


def buscar_pedido(codigo):
    """
    Busca un pedido por su código.

    Retorna:
        dict con el pedido, o None si no existe.
    """
    pedidos = leer_json(ARCHIVO)
    for pedido in pedidos:
        if pedido["codigo"] == codigo:
            return pedido
    return None


def listar_pedidos():
    """
    Retorna la lista completa de pedidos registrados.
    """
    return leer_json(ARCHIVO)


def listar_pedidos_pendientes():
    """
    Retorna la lista de pedidos cuyo estado es 'pendiente'.
    """
    pedidos = leer_json(ARCHIVO)
    return [p for p in pedidos if p["estado"] == "pendiente"]


def cambiar_estado_pedido(codigo, nuevo_estado):
    """
    Cambia el estado de un pedido, validando que el estado sea uno de los
    estados permitidos. Usada también internamente por el módulo despacho.

    Retorna:
        True si se actualizó, False si el pedido no existe o el estado es inválido.
    """
    if nuevo_estado not in ESTADOS_VALIDOS:
        print(f"Error: estado '{nuevo_estado}' no es válido. Use uno de {ESTADOS_VALIDOS}.")
        return False

    pedidos = leer_json(ARCHIVO)
    for pedido in pedidos:
        if pedido["codigo"] == codigo:
            pedido["estado"] = nuevo_estado
            escribir_json(ARCHIVO, pedidos)
            print(f"Pedido {codigo} actualizado a estado '{nuevo_estado}'.")
            return True

    print(f"Error: el pedido {codigo} no existe.")
    return False
