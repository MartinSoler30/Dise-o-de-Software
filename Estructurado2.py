def main():

    productos = []

    numero_productos = int(input("Digite el número de productos: "))

    for i in range(numero_productos):
        print(f"\nProducto {i + 1}:")

        codigo = input("Código del producto: ")
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio unitario: "))
        cantidad = int(input("Cantidad vendida: "))

        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio_unitario": precio,
            "cantidad_vendida": cantidad
        }

        productos.append(producto)

    total_general = 0

    for prod in productos:

        total_producto = (
            prod["precio_unitario"] *
            prod["cantidad_vendida"]
        )

        print(f"\nProducto: {prod['nombre']}")
        print(f"Total producto: {total_producto}")

        total_general += total_producto

    print("\n--------------------------------")
    print("TOTAL GENERAL DE VENTAS:", total_general)
    print("--------------------------------")


if __name__ == "__main__":
    main()