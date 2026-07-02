"""
reportes.py
-----------
Responsable: Estudiante 5 (rol: Responsable de reportes)

Funciones:
    contar_no_entregados()
    pedidos_por_estado()
    porcentaje_retrasos()
    total_pedidos()
    listar_pedidos_criticos()
"""

from modulos.pedidos import listar_pedidos, ESTADOS_VALIDOS


def total_pedidos():
    """
    Retorna la cantidad total de pedidos registrados.
    """
    return len(listar_pedidos())


def pedidos_por_estado():
    """
    Calcula cuántos pedidos hay en cada estado.

    Retorna:
        dict, por ejemplo:
        {"pendiente": 3, "en_ruta": 1, "entregado": 5,
         "retrasado": 0, "no_entregado": 2}
    """
    conteo = {estado: 0 for estado in ESTADOS_VALIDOS}
    for pedido in listar_pedidos():
        estado = pedido.get("estado")
        if estado in conteo:
            conteo[estado] += 1
    return conteo


def contar_no_entregados():
    """
    Retorna la cantidad de pedidos en estado 'no_entregado'.
    """
    return pedidos_por_estado()["no_entregado"]


def porcentaje_retrasos():
    """
    Calcula el porcentaje de pedidos en estado 'retrasado' respecto
    al total de pedidos.

    Fórmula:
        (pedidos_retrasados / total_pedidos) * 100

    Retorna:
        float redondeado a 2 decimales. 0.0 si no hay pedidos.
    """
    total = total_pedidos()
    if total == 0:
        return 0.0
    retrasados = pedidos_por_estado()["retrasado"]
    return round((retrasados / total) * 100, 2)


def listar_pedidos_criticos():
    """
    Retorna la lista de pedidos que están en estado 'retrasado' o
    'no_entregado', es decir, los que requieren atención inmediata.
    """
    return [p for p in listar_pedidos() if p["estado"] in ("retrasado", "no_entregado")]


def imprimir_resumen():
    """
    Imprime en consola un resumen general de indicadores.
    Función de conveniencia usada desde el menú principal.
    """
    print("\n--- RESUMEN DE INDICADORES ---")
    print(f"Total de pedidos: {total_pedidos()}")
    for estado, cantidad in pedidos_por_estado().items():
        print(f"  - {estado}: {cantidad}")
    print(f"Porcentaje de pedidos retrasados: {porcentaje_retrasos()}%")
    print(f"Pedidos no entregados: {contar_no_entregados()}")
    criticos = listar_pedidos_criticos()
    print(f"Pedidos críticos (retrasados o no entregados): {len(criticos)}")
