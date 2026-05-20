class Producto:

    def __init__(self, codigo, nombre, precio_unitario, cantidad_vendida):

        self.codigo = codigo
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad_vendida = cantidad_vendida

    def total_producto(self):

        return self.precio_unitario * self.cantidad_vendida


def main():

    productos = []

    cantidad_productos = int(input("Digite la cantidad de productos: "))

    for i in range(cantidad_productos):

        print(f"\nProducto {i + 1}:")

        codigo = input("Digite el código del producto: ")
        nombre = input("Digite el nombre del producto: ")
        precio = float(input("Digite el precio unitario: "))
        cantidad = int(input("Digite la cantidad vendida: "))

        producto = Producto(
            codigo,
            nombre,
            precio,
            cantidad
        )

        productos.append(producto)

    total_general = sum(
        prod.total_producto()
        for prod in productos
    )

    print("\nDETALLE DE VENTAS")

    for prod in productos:

        print(f"\nProducto: {prod.nombre}")
        print(f"Total producto: {prod.total_producto()}")

    print("\n--------------------------------")
    print(f"TOTAL GENERAL DE VENTAS: {total_general}")
    print("--------------------------------")


if __name__ == "__main__":
    main()