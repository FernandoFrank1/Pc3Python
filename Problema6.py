# Problema 6

class Producto:
    def __init__(self, nombre, codigo, precio, año):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}, Precio: {self.precio}, Año: {self.año}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
        else:
            raise TypeError("Se esperaba un objeto de tipo Producto")

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            return productos_filtrados
        else:
            print("No se encontraron productos para el año especificado.")
            return []


if __name__ == "__main__":
    catalogo = Catalogo()

    try:
        producto1 = Producto("Polarizado", "12345", 25.99, 2022)
        producto2 = Producto("Puerta", "67890", 55.50, 2023)
        producto3 = Producto("Parachoque", "54321", 80.00, 2022)

        catalogo.agregar_producto(producto1)
        catalogo.agregar_producto(producto2)
        catalogo.agregar_producto(producto3)

        print("Lista de productos:")
        catalogo.mostrar_productos()

        año_filtro = int(input("\nIngrese el año para filtrar los productos: "))
        print(f"\nFiltrando productos para el año {año_filtro}:")
        productos_filtrados = catalogo.filtrar_por_año(año_filtro)
        for producto in productos_filtrados:
            print(producto)

    except TypeError as e:
        print(f"Error: {e}")
