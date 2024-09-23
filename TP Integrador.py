# Sistema de Gestión para una Ferretería - Hito 1 

import sys

# Diccionario de productos donde la clave será el código del producto
# Cada valor en el diccionario será una tupla con (nombre, categoría, precio, stock)
productos = {}

# Conjunto para almacenar las categorías de productos, sin duplicados
categorias = set()

def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\n--- Sistema de Gestión para Ferretería ---")
    print("Seleccione una opción:")
    print("1. Crear Material")
    print("2. Ingresar Stock")
    print("3. Actualizar Precio")
    print("4. Registrar Venta")
    print("5. Mostrar Productos")
    print("6. Mostrar Categorías")
    print("7. Salir")

def crear_material():
    """
    Permite al usuario crear un nuevo material ingresando los detalles necesarios.
    """
    codigo = int(input("Ingrese el código del producto (número entero): "))
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad en stock: "))

    if codigo in productos:
        print(f"\nADVERTENCIA ERROR !!! YA EXISTE UN PRODUCTO CON ESE MISMO CODIGO !!! {codigo}.")
        return

    productos[codigo] = (nombre, categoria, precio, stock)
    categorias.add(categoria)

    print(f"\nProducto '{nombre}' agregado exitosamente.\n")

def ingresar_stock():
    """
    Permite al usuario agregar stock a un producto existente.
    Busca el producto en el diccionario por su código.
    """
    codigo = int(input("Ingrese el código del producto para agregar stock: "))
    cantidad = int(input("Ingrese la cantidad a agregar: "))

    producto = productos.get(codigo)
    
    if producto:
        # Utilizamos rebanada para acceder al stock actual
        nombre, categoria, precio, stock = producto
        productos[codigo] = (nombre, categoria, precio, stock + cantidad)
        print(f"\nStock de '{nombre}' actualizado. Nuevo stock: {productos[codigo][3]}\n")
    else:
        print(f"\nProducto con código {codigo} no encontrado.\n")

def actualizar_precio():
    """
    Permite al usuario actualizar el precio de un producto existente.
    Busca el producto en el diccionario por su código.
    """
    codigo = int(input("Ingrese el código del producto para actualizar el precio: "))
    nuevo_precio = float(input("Ingrese el nuevo precio: "))

    if codigo in productos:
        # Utilizamos rebanada para acceder al precio
        nombre, categoria, _, stock = productos[codigo]
        productos[codigo] = (nombre, categoria, nuevo_precio, stock)
        print(f"\nPrecio de '{nombre}' actualizado a ${nuevo_precio:.2f}\n")
    else:
        print(f"\nProducto con código {codigo} no encontrado.\n")

def registrar_venta():
    """
    Permite al usuario registrar una venta, reduciendo el stock del producto correspondiente.
    Busca el producto en el diccionario por su código.
    """
    codigo = int(input("Ingrese el código del producto vendido: "))
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))

    producto = productos.get(codigo)
    
    if not producto:
        print(f"\nProducto con código {codigo} no encontrado.\n")
        return

    nombre, categoria, precio, stock = producto
    
    if stock < cantidad_vendida:
        print(f"\nStock insuficiente para el producto '{nombre}'.\n")
        return

    # Actualizamos el stock
    productos[codigo] = (nombre, categoria, precio, stock - cantidad_vendida)
    print(f"\nVenta registrada. Nuevo stock de '{nombre}': {productos[codigo][3]}\n")

def construir_matriz_productos():
    """
    Construye una matriz con todos los productos. Cada fila de la matriz representa un producto,
    y cada columna contiene una parte del nombre, categoría, precio o stock.
    La matriz se organiza por el código de producto de menor a mayor.
    """
    # Definimos los anchos máximos para cada columna
    max_ancho_nombre = 25
    max_ancho_categoria = 25
    

    # Matriz donde guardaremos cada fila de producto
    matriz_productos = []

    # Ordenamos los productos por el código antes de construir la matriz
    productos_ordenados = sorted(productos.items())

    for codigo, (nombre, categoria, precio, stock) in productos_ordenados:
        # Rebanamos el nombre y la categoría para ajustarlos a los anchos máximos
        nombre_partes = [nombre[i:i + max_ancho_nombre] for i in range(0, len(nombre), max_ancho_nombre)]
        categoria_partes = [categoria[i:i + max_ancho_categoria] for i in range(0, len(categoria), max_ancho_categoria)]
        
        # Creamos una fila con las primeras partes del nombre y la categoría
        fila = [str(codigo), nombre_partes[0], categoria_partes[0], f"${precio:<9.2f}", str(stock)]
        matriz_productos.append(fila)

        # Añadimos más filas para las partes restantes del nombre y categoría si son muy largos
        max_filas = max(len(nombre_partes), len(categoria_partes))
        for i in range(1, max_filas):
            nombre_linea = nombre_partes[i] if i < len(nombre_partes) else ""
            categoria_linea = categoria_partes[i] if i < len(categoria_partes) else ""
            matriz_productos.append(["", nombre_linea, categoria_linea, "", ""])

    return matriz_productos

def mostrar_productos():
    """
    Muestra la matriz de productos, ajustando el ancho de las columnas y respetando el formato de filas.
    Los productos se muestran en orden de código.
    """
    matriz_productos = construir_matriz_productos()
    max_ancho_nombre = 25
    max_ancho_categoria = 25
    max_ancho_precio = 20
    max_ancho_stock = 10
    # Encabezado de la tabla
    print("\n--- Catálogo de Productos ---")
    print(f"{{:<10}} {{:<{max_ancho_nombre}}} {{:<{max_ancho_categoria}}} {{:<{max_ancho_precio}}} {{:<{max_ancho_stock}}}".format('Código', 'Nombre', 'Categoría', 'Precio', 'Stock'))
    print("-" * 65)

    # Mostramos cada fila de la matriz
    for fila in matriz_productos:
        print(f"{{:<10}} {{:<{max_ancho_nombre}}} {{:<{max_ancho_categoria}}} {{:<{max_ancho_precio}}} {{:<{max_ancho_stock}}}".format(fila[0], fila[1], fila[2], fila[3], fila[4]))


def mostrar_categorias():
    """
    Muestra el conjunto de categorías de productos.
    """
    if not categorias:
        print("\nNo hay categorías registradas.\n")
        return

    print("\n--- Categorías de Productos ---")
    for categoria in categorias:
        print(f"- {categoria}")
    print()

def main():
    """
    Función principal que ejecuta el menú y llama a las funciones correspondientes según la opción elegida.
    """
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            crear_material()
        elif opcion == '2':
            ingresar_stock()
        elif opcion == '3':
            actualizar_precio()
        elif opcion == '4':
            registrar_venta()
        elif opcion == '5':
            mostrar_productos()
        elif opcion == '6':
            mostrar_categorias()
        elif opcion == '7':
            print("\nSaliendo del sistema. ¡Hasta luego!\n")
            sys.exit()
        else:
            print("\nOpción inválida. Por favor, seleccione una opción del 1 al 7.\n")


# Ejecutamos la función principal al iniciar el programa
if __name__ == "__main__":
    main()
