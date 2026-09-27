inventario = {}

ventas_del_dia = []

#Menu pricipal 

def menu():

    while True:
        print(" FERRETERIA - INVENTARIO")
        print("1. agregar producto")
        print("2. consultar inventario ")
        print("3. buscar producto ")
        print("4. vender producto ")
        print("5. reporte de stock bajo ")
        print("6. ver venyas del dia ")
        print("7. ver total vendido ")
        print("8. salir ")

        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            consultar_inventario()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            vender_producto()

        elif opcion == "5":
            stock_bajo()

        elif opcion == "6":
            ver_ventas()

        elif opcion == "7":
            total_vendido()

        elif opcion == "8":
            guardar_inventario()
            print("programa finazlizado ")
            break
        else:
            print("opcion incorrecta. Selecciona del 1 al 8")

#Agregar producto 
def agregar_producto():
    print("AGREGAR PRODUCTO")
    nombre = input("Nombre del producto: ")
    nombe = nombre.strip()
    if nombre == "":
        print("Debes escribir el nombre del producto ")
        return

    nombre_busqueda = nombre.lower
    existe = False

    for clave in inventario:
        if clave == nombre_busqueda: 
            existe = True  

    if existe == True:
        print("Ese producto ya existe en el inventario ")
        return

    try:

        # Pedimos el precio
        precio = float(input("Precio del producto: $"))

        # El precio debe ser mayor que 0
        if precio <= 0:
            print("El precio debe ser mayor a 0.")
            return

        # Pedimos la cantidad inicial
        cantidad = int(input("Cantidad inicial: "))

        # La cantidad no puede ser negativa
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return

        # Guardamos los datos en el diccionario
        inventario[nombre_busqueda] = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        print("Producto agregado correctamente.")

    # Si el usuario escribe letras
    
    except ValueError:
        print("Debes ingresar números válidos.")


