codigos = []
nombres = []
precios_unitarios = []
cantidades_vendidas = []

numero_productos = int(input("Digite el número de productos: "))

for i in range(numero_productos):
    print(f"Producto {i + 1}:")

    codigo = input("Digite el código del producto: ")
    nombre = input("Digite el nombre del producto: ")
    precio = float(input("Digite el precio unitario: "))
    cantidad = int(input("Digite la cantidad vendida: "))

    codigos.append(codigo)
    nombres.append(nombre)
    precios_unitarios.append(precio)
    cantidades_vendidas.append(cantidad)

total_general = 0

for i in range(numero_productos):
    total_producto = precios_unitarios[i] * cantidades_vendidas[i]

    print(f"\nProducto: {nombres[i]}")
    print(f"Total producto: {total_producto}")

    total_general = total_general + total_producto

print("\n--------------------------------")
print("TOTAL GENERAL DE VENTAS:", total_general)
print("--------------------------------")