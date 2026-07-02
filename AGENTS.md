# AGENTS.md — Sistema de Control de Pedidos No Entregados

## Objetivo del proyecto
Software en Python para registrar clientes, productos y pedidos, controlar
stock, asignar despachos y generar reportes de pedidos entregados,
pendientes, retrasados y no entregados.

## Estructura de carpetas
proyecto_pedidos/
├── main.py                  # Menú principal (integrador)
├── datos/                   # Persistencia en JSON
│   ├── clientes.json
│   ├── productos.json
│   └── pedidos.json
├── modulos/
│   ├── almacenamiento.py    # lectura/escritura JSON compartida
│   ├── clientes.py
│   ├── productos.py
│   ├── stock.py
│   ├── pedidos.py
│   ├── despacho.py
│   └── reportes.py
└── evidencias/               # prompts, bitácora, casos de prueba

## Cómo ejecutar el programa
1. Ubicarse en la carpeta proyecto_pedidos/
2. Ejecutar: python main.py
3. Navegar el menú principal y los submenús por número de opción.

## Estados válidos de un pedido
pendiente, en_ruta, entregado, retrasado, no_entregado

## Reglas de codificación
- Cada módulo solo contiene funciones relacionadas con su responsabilidad.
- Las funciones deben tener nombre, parámetros y retorno claros.
- Toda función que modifica datos debe validar sus parámetros antes de escribir.
- No duplicar lógica de lectura/escritura: usar siempre almacenamiento.py.
- No usar librerías externas innecesarias (solo librería estándar).

## Qué significa "terminado"
- El programa inicia sin errores con `python main.py`.
- Los cinco módulos están integrados en el menú principal.
- Se puede registrar un cliente, un producto, un pedido, asignar despacho
  y ver los reportes sin que el programa se detenga por errores.
- Cada función fue probada con al menos un caso válido y un caso inválido.
- El uso de IA está documentado en evidencias/prompts_utilizados.
