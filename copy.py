inventario = {}

ventas_dia = []

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

        #Pedimos el precio
        precio = float(input("Precio del producto: $"))

        #El precio debe ser mayor que 0
        if precio <= 0:
            print("El precio debe ser mayor a 0.")
            return

        #Pedimos la cantidad inicial
        cantidad = int(input("Cantidad inicial: "))

        #La cantidad no puede ser negativa
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return

        #Guardamos los datos en el diccionario
        inventario[nombre_busqueda] = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        print("\nProducto agregado correctamente.")
        print("Nombre:", nombre)
        print("Precio: $", precio)
        print("Cantidad:", cantidad)

    #Si el usuario escribe letras
    
    except ValueError:
        print("Debes ingresar numeros validos.")

#Consultar inventario 

def consultar_inventario():
    print("Inventario")

    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    #Recorremos todos los productos
    for clave in inventario:

        #Obtenemos los datos del producto
        producto = inventario[clave]

       
        print("Producto:", producto["nombre"])
        print("Precio: $", producto["precio"])
        print("Cantidad:", producto["cantidad"])

#Vender producto 
def vender_producto():

    print("\n--- VENDER PRODUCTO ---")

    #Pedimos el producto que se desea vender
    nombre = input("Nombre del producto: ")

    #Quitamos espacios
    nombre = nombre.strip()

    #Convertimos a minusculas para buscar
    nombre_busqueda = nombre.lower()

    #Esta variable guardara la clave encontrada
    clave_encontrada = ""

    #Buscamos el producto en el inventario
    for clave in inventario:

        if clave == nombre_busqueda:
            clave_encontrada = clave

    #Si quedo vacia significa que no existe
    if clave_encontrada == "":
        print("El producto no existe.")
        return

    try:

        #Pedimos la cantidad que desea comprar
        cantidad = int(input("Cantidad a vender: "))

        #La cantidad debe ser mayor a cero
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        #Obtenemos los datos del producto
        producto = inventario[clave_encontrada]

        #Revisamos si existe suficiente mercancia
        if cantidad > producto["cantidad"]:

            print("No hay suficiente producto disponible.")
            print("Existencia actual:", producto["cantidad"])

            return

        #Calculamos el total de la venta
        total = producto["precio"] * cantidad

        #Restamos las unidades vendidas
        producto["cantidad"] = producto["cantidad"] - cantidad

        #Creamos un diccionario para guardar la venta
        venta = {
            "producto": producto["nombre"],
            "cantidad": cantidad,
            "precio": producto["precio"],
            "total": total
        }

        #Agregamos la venta a la lista
        ventas_dia.append(venta)

        print("\nVenta realizada correctamente.")
        print("Producto:", producto["nombre"])
        print("Cantidad:", cantidad)
        print("Precio unitario: $", producto["precio"])
        print("Total: $", total)

    #Evitamos que el programa se rompa
    
    except ValueError:
        print("Debes ingresar una cantidad valida.")

#Buscar producto 

def buscar_producto():
    print("BUSCAR PRODUCTO")
    nombre = input("Nombre del producto: ")
    nombre = nombre.strip()
    nombre_busqueda = nombre.lower()
    #Variable para saber si encontramos el producto
    encontrado = False

    #Recorremos el inventario
    for clave in inventario:

        #Comparamos las claves
        if clave == nombre_busqueda:

            producto = inventario[clave]

            print("\nProducto encontrado:")
            print("Nombre:", producto["nombre"])
            print("Precio: $", producto["precio"])
            print("Cantidad disponible:", producto["cantidad"])

            encontrado = True

    #Si despues de recorrer el inventario
    #sigue siendo falso, no existe
    if encontrado == False:
        print("El producto no existe.")

#Reporte de stock bajo 

def stock_bajo():
    print("PRODUCTOS CON STOCK BAJO ")
    #Variable que indica si encontramos un producto cin bajon stock
    encontrado = False

    #Recorremos el inventario
    for clave in inventario:

        producto = inventario[clave]

        #Si tiene 5 unidades o menos = stcok bajo 
        
        if producto["cantidad"] <= 5:

            print("Producto:", producto["nombre"])
            print("Cantidad:", producto["cantidad"])

            encontrado = True

    #Si no encontramos ninguno
    if encontrado == False:
        print("No hay productos con stock bajo.")

#Ver ventas del dia 

def ver_ventas():
    print("VENTAS DEL DIA ")
    #Revisamos si la lista esta vacia
    if len(ventas_dia) == 0:
        print("Todavia no se han realizado ventas.")
        return

    #Recorremos todas las ventas
    for venta in ventas_dia:

        
        print("Producto:", venta["producto"])
        print("Cantidad:", venta["cantidad"])
        print("Total: $", venta["total"])

def total_vendido():
    print("TOTAL VENDIDO ")
     #Empezamos el total en cero
    total = 0

    #Recorremos las ventas
    for venta in ventas_dia:

        #Sumamos cada venta al total
        total = total + venta["total"]

    print("Total vendido: $", total)

#Guardar inventario 

def guardar_inventario():
    #Abrimos el archivo en modo escritura
    archivo = open("inventario.txt", "w")

    #Recorremos los productos
    for clave in inventario:

        producto = inventario[clave]

        #Convertimos precio y cantidad a texto
        precio_texto = str(producto["precio"])
        cantidad_texto = str(producto["cantidad"])

        #Creamos la linea que se guardara
        linea = producto["nombre"] + "|"
        linea = linea + precio_texto + "|"
        linea = linea + cantidad_texto + "\n"

        #Escribimos la linea en el archivo
        archivo.write(linea)

    #Cerramos el archivo
    archivo.close()

    print("Inventario guardado correctamente.")








    


