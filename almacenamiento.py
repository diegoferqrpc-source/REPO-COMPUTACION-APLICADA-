"""
clientes.py
-----------
Responsable: Estudiante 1 (rol: Responsable de pedidos / clientes)

Funciones para registrar y consultar clientes.
Persistencia en datos/clientes.json
"""

from modulos.almacenamiento import leer_json, escribir_json, generar_id

ARCHIVO = "clientes.json"


def registrar_cliente(nombre, telefono, direccion):
    """
    Registra un nuevo cliente.

    Parametros:
        nombre (str): nombre completo del cliente.
        telefono (str): teléfono de contacto.
        direccion (str): dirección de entrega.

    Retorna:
        dict: el cliente creado, con su id asignado.
        None: si los datos no son válidos.
    """
    if not nombre or not nombre.strip():
        print("Error: el nombre del cliente no puede estar vacío.")
        return None
    if not telefono or not telefono.strip():
        print("Error: el teléfono del cliente no puede estar vacío.")
        return None

    clientes = leer_json(ARCHIVO)
    nuevo_cliente = {
        "id": generar_id(clientes, "id"),
        "nombre": nombre.strip(),
        "telefono": telefono.strip(),
        "direccion": direccion.strip() if direccion else "",
    }
    clientes.append(nuevo_cliente)
    escribir_json(ARCHIVO, clientes)
    print(f"Cliente registrado con id {nuevo_cliente['id']}.")
    return nuevo_cliente


def buscar_cliente(cliente_id):
    """
    Busca un cliente por su id.

    Retorna:
        dict con los datos del cliente, o None si no existe.
    """
    clientes = leer_json(ARCHIVO)
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente
    return None


def listar_clientes():
    """
    Retorna la lista completa de clientes registrados.
    """
    return leer_json(ARCHIVO)


def existe_cliente(cliente_id):
    """
    Retorna True si el cliente existe, False si no.
    Se usa como validación desde el módulo de pedidos.
    """
    return buscar_cliente(cliente_id) is not None
