class TiendaVirtual:
    def __init__(self):
        # Inicializamos el catálogo de productos
        self.catalogo = {
            'Laptop': 15000,
            'Smartphone': 8000,
            'Audífonos': 1500,
            'Monitor': 6000,
            'Teclado': 800
        }
        # Inicializamos un carrito vacío
        self.carrito = {}

    # Mostrar el catálogo de productos
    def mostrar_catalogo(self):
        print("\n--- Catálogo de Productos ---")
        for producto, precio in self.catalogo.items():
            print(f"{producto}: ${precio}")
        print("-----------------------------")

    # Agregar productos al carrito
    def agregar_al_carrito(self, producto, cantidad):
        if producto in self.catalogo:
            if producto in self.carrito:
                self.carrito[producto] += cantidad  # Si ya existe en el carrito, sumamos la cantidad
            else:
                self.carrito[producto] = cantidad  # Si no está en el carrito, lo agregamos
            print(f"{cantidad} unidad(es) de {producto} agregada(s) al carrito.")
        else:
            print(f"El producto '{producto}' no está disponible en el catálogo.")

    # Ver los productos en el carrito
    def ver_carrito(self):
        if not self.carrito:
            print("Tu carrito está vacío.")
        else:
            print("\n--- Carrito de Compras ---")
            for producto, cantidad in self.carrito.items():
                print(f"{producto}: {cantidad} unidad(es)")
            print("--------------------------")

    # Calcular el total del carrito
    def calcular_total(self):
        total = 0
        for producto, cantidad in self.carrito.items():
            total += self.catalogo[producto] * cantidad
        return total

    # Proceder al pago
    def pagar(self):
        if not self.carrito:
            print("Tu carrito está vacío. No puedes proceder al pago.")
        else:
            total = self.calcular_total()
            print(f"El total de tu compra es: ${total}")
            confirmar = input("¿Deseas proceder con el pago? (s/n): ")
            if confirmar.lower() == 's':
                print("¡Gracias por tu compra! Tu pedido ha sido realizado.")
                self.carrito.clear()  # Vaciamos el carrito después de la compra
            else:
                print("Has cancelado el pago.")

# Función principal para interactuar con la tienda
def ejecutar_tienda():
    tienda = TiendaVirtual()
    
    while True:
        print("\n--- Menú de la Tienda Virtual ---")
        print("1. Ver catálogo de productos")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito de compras")
        print("4. Pagar")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            tienda.mostrar_catalogo()
        elif opcion == '2':
            producto = input("Ingresa el nombre del producto que deseas agregar: ")
            try:
                cantidad = int(input(f"¿Cuántas unidades de {producto} deseas agregar?: "))
                tienda.agregar_al_carrito(producto, cantidad)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == '3':
            tienda.ver_carrito()
        elif opcion == '4':
            tienda.pagar()
        elif opcion == '5':
            print("Gracias por visitar la tienda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona nuevamente.")

# Ejecutar la tienda virtual
if __name__ == '__main__':
    ejecutar_tienda()
