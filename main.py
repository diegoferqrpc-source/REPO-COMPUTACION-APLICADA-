"""
main.py
-------
Responsable: Estudiante 6 (rol: Integrador del proyecto)

Menú principal del Sistema de Control de Pedidos No Entregados.
Conecta los módulos: clientes, productos, stock, pedidos, despacho y reportes.
No reescribe la lógica interna de cada módulo, solo la organiza.
"""

from modulos import clientes, productos, stock, pedidos, despacho, reportes


def leer_entero(mensaje):
    """Pide un número entero al usuario, validando el formato."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print("Por favor ingrese un número entero válido.")


def menu_clientes():
    while True:
        print("\n--- MENÚ CLIENTES ---")
        print("1. Registrar cliente")
        print("2. Buscar cliente")
        print("3. Listar clientes")
        print("0. Volver")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            clientes.registrar_cliente(nombre, telefono, direccion)
        elif opcion == "2":
            cid = leer_entero("ID del cliente: ")
            cliente = clientes.buscar_cliente(cid)
            print(cliente if cliente else "Cliente no encontrado.")
        elif opcion == "3":
            for c in clientes.listar_clientes():
                print(c)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def menu_stock():
    while True:
        print("\n--- MENÚ PRODUCTOS Y STOCK ---")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Agregar stock")
        print("4. Descontar stock")
        print("5. Ver productos con stock bajo")
        print("0. Volver")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: ") or 0)
            stock_inicial = leer_entero("Stock inicial: ")
            productos.registrar_producto(nombre, precio, stock_inicial)
        elif opcion == "2":
            for p in productos.listar_productos():
                print(p)
        elif opcion == "3":
            pid = leer_entero("ID del producto: ")
            cantidad = leer_entero("Cantidad a agregar: ")
            stock.agregar_stock(pid, cantidad)
        elif opcion == "4":
            pid = leer_entero("ID del producto: ")
            cantidad = leer_entero("Cantidad a descontar: ")
            stock.descontar_stock(pid, cantidad)
        elif opcion == "5":
            minimo = leer_entero("Mostrar productos con stock menor o igual a: ")
            for p in stock.mostrar_stock_bajo(minimo):
                print(p)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def menu_pedidos():
    while True:
        print("\n--- MENÚ PEDIDOS ---")
        print("1. Registrar pedido")
        print("2. Buscar pedido")
        print("3. Listar todos los pedidos")
        print("4. Listar pedidos pendientes")
        print("0. Volver")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            cid = leer_entero("ID del cliente: ")
            lista_productos = []
            while True:
                pid = leer_entero("ID del producto (0 para terminar): ")
                if pid == 0:
                    break
                cantidad = leer_entero("Cantidad: ")
                lista_productos.append({"producto_id": pid, "cantidad": cantidad})
            pedidos.registrar_pedido(cid, lista_productos)
        elif opcion == "2":
            codigo = leer_entero("Código del pedido: ")
            pedido = pedidos.buscar_pedido(codigo)
            print(pedido if pedido else "Pedido no encontrado.")
        elif opcion == "3":
            for p in pedidos.listar_pedidos():
                print(p)
        elif opcion == "4":
            for p in pedidos.listar_pedidos_pendientes():
                print(p)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def menu_despacho():
    while True:
        print("\n--- MENÚ DESPACHO ---")
        print("1. Asignar repartidor a pedido")
        print("2. Registrar entrega exitosa")
        print("3. Marcar pedido como retrasado")
        print("4. Registrar motivo de no entrega")
        print("0. Volver")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            codigo = leer_entero("Código del pedido: ")
            repartidor = input("Nombre del repartidor: ")
            despacho.asignar_despacho(codigo, repartidor)
        elif opcion == "2":
            codigo = leer_entero("Código del pedido: ")
            despacho.registrar_entrega(codigo)
        elif opcion == "3":
            codigo = leer_entero("Código del pedido: ")
            despacho.actualizar_estado(codigo, "retrasado")
        elif opcion == "4":
            codigo = leer_entero("Código del pedido: ")
            motivo = input("Motivo de no entrega: ")
            despacho.registrar_motivo_no_entrega(codigo, motivo)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def menu_reportes():
    reportes.imprimir_resumen()
    input("\nPresione Enter para volver al menú principal...")


def menu_principal():
    while True:
        print("\n===== SISTEMA DE CONTROL DE PEDIDOS NO ENTREGADOS =====")
        print("1. Gestión de clientes")
        print("2. Gestión de productos y stock")
        print("3. Gestión de pedidos")
        print("4. Gestión de despacho")
        print("5. Reportes e indicadores")
        print("0. Salir")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_stock()
        elif opcion == "3":
            menu_pedidos()
        elif opcion == "4":
            menu_despacho()
        elif opcion == "5":
            menu_reportes()
        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    menu_principal()
