from datetime import date
from enum import Enum


def main():
    print("1. Inventario")
    print("2. Atención al cliente")
    print("3. Reportes")
    print("4. Pedidos")
    print("5. Reservaciones")
    print("6. Salir")

    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        print("Inventario")
        print("1. Salir")
        print("2. Mostrar sedes")
        opcion2 = int(input("Elija una opción: "))
        if opcion2 == 2:
            print("1. Envigado")
            print("2. Sandiego")
            print("3. Belen")
            print("4. La America")
            opcion3 = int(input("Elija una sede: "))

            restaurante = Restaurante.sedes[opcion3 - 1]
            if restaurante.mostrarItemsVencidos():
                print("Los siguientes artículos están vencidos y se eliminarán:")
                for item in restaurante.mostrarItemsVencidos():
                    print(item)
                restaurante.eliminarVencidos()
                print("Inventario vencido eliminado")

            while True:
                print("1. Mostrar inventario")
                print("2. Precio artículo inventario")
                print("3. Revisar niveles de Stock")
                print("4. Registrar artículo en inventario")
                print("5. Renovar inventario")
                print("6. Valor del inventario total")
                print("7. Salir")
                opcion4 = int(input("Elija una opción: "))

                if opcion4 == 1:
                    print("Inventario:")
                    for item, cantidad in restaurante.inventario.diccionarioItems.items():
                        print(f"{item}: {cantidad}")
                elif opcion4 == 2:
                    item = input("Nombre del artículo: ")
                    precio = float(input("Precio del artículo: "))
                    print(f"Precio del artículo {item} en el inventario es de ${precio}")
                elif opcion4 == 3:
                    sin_stock = restaurante.inventario.obtenerItemsSinStock()
                    if sin_stock:
                        print("Los siguientes artículos están sin stock:")
                        for item in sin_stock:
                            print(item)
                    else:
                        print("No hay artículos sin stock")
                elif opcion4 == 4:
                    nombre = input("Nombre del artículo: ")
                    cantidad = int(input("Cantidad del artículo: "))
                    precio = float(input("Precio del artículo: "))
                    fecha_vencimiento = input("Fecha de vencimiento del artículo (YYYY-MM-DD): ")
                    item = Item(nombre, cantidad, precio, fecha_vencimiento, restaurante.inventario)
                    print(f"Artículo {nombre} registrado en el inventario")
                elif opcion4 == 5:
                    restaurante.inventario.resetearInventario()
                    print("Inventario renovado")
                elif opcion4 == 6:
                    valor_total = 0
                    for item, cantidad in restaurante.inventario.diccionarioItems.items():
                        valor_total += cantidad * item.precio
                    print(f"Valor total del inventario: ${valor_total:.2f}")
                elif opcion4 == 7:
                    break
    elif opcion == 2:
        print("Atención al cliente")
        print("1. Salir")
        opcion5 = int(input("Elija una opción: "))
        if opcion5 == 1:
            pass
    elif opcion == 3:
        print("Reportes")
        print("1. Salir")
        opcion6 = int(input("Elija una opción: "))
        if opcion6 == 1:
            pass



    elif opcion == 4:
        print("Pedidos")
        print("1. Pedido de envio")
        print("2. Pedido para recoger")
        print("3. Acceso de administrador")
        print("4. Salir")
        opcion7 = int(input("Elija una opción: "))

        #inicia la funcionalidad
        #Opciones para el pedido de envio
        if opcion7 == 1:
            print("Ha seleccionado la opción 1")
            print("Por favor, ingrese sus datos personales")
            nombre = input("Dijite su nombre: ")
            apellido = input("Dijite su apellido: ")
            print(f"Usted a ingresado estos datos: nombre: {nombre}, apellido: {apellido}" )
            print("¿Desea confirmar sus datos personales?")
            confir1 = str(input())

            if confir1 == "Y":
                print("Datos confirmados")
                print("Por favor, escriba su dirección de residencia")
                direccion = str(input())
                ubicacion = Pedido.Direccion(direccion)
                print(f"Ha ingresado la dirección: {ubicacion}.")
                print("¿Desea confirmar su dirección?")
                confir = str(input())

                if confir == "Y":
                    print("Dirección confirmada")
                    print("¿Que desea ordenar?")
                    #metodo para mostrar el muenu del restaurante
                    print("Productos seleccionados ¿desea agragar algo más?")
                    confir3 = str(input())
                    if confir3 == "Y":
                        #metodo para agregar algo mas al pedido
                        pass
                        
                    elif confir3 == "N":
                        print("Productos seleccionados")
                        print("El total de su compra es: ")
                        #metodo para mostrar el total de la compra mas un adicional por el domicilio 

                    else:
                        pass

                elif confir == "N":
                    print("Direccion no confirmada, ahora puede editar la dirección")
                    #metodo para cambiar la dirección
                    print("¿Desea confirmar los nuevos datos ingresados?")
                    confir2 = str(input())
                    if confir2 == "Y":
                        #se sigue con el curso de la funcionalidad
                        pass
                    elif confir2 == "N":
                        #METODO PARA CAMBIAR LOS DATOS INGRESADOS
                        pass
                    else:
                        print("Opción invalida, vuelva a intentarlo")
                else:
                    print("Error, opción invalida, vuelva a intentarlo") 

            elif confir1 == "N":
                print("Datos no confirmados, ahora puede editar los datos ingresados")  
                 #metodo para cambiar la dirección

            else:
                print("Opción invalida, por favor intentarlo nuevamente")  

        #opciones para el pedido para recoger  
        elif opcion7 == 2:
            print("Ha seleccionado la opción 2")
            print("Por favor, ingrese sus datos personales")
            nombre = input("Dijite su nombre: ")
            apellido = input("Dijite su apellido: ")
            print(f"Usted a ingresado estos datos: nombre: {nombre}, apellido: {apellido}" )
            print("¿Desea confirmar sus datos personales?")
            confir1 = str(input())

            if confir1 == "Y":
                print("Datos confirmados")

            elif confir1 == "N":
                print("Datos no confirmados, ahora puede editar los datos ingresados")  
                 #metodo para cambiar la dirección

            else:
                pass

        #Opciones para entrada como administrador            
        elif opcion7 == 3:
            print("Ha seleccionado la opción 3")

        #opciones de salida
        else:
            pass           









    elif opcion == 5:
        print("Reservaciones")
        print("1. Salir")
        opcion8 = int(input("Elija una opción: "))
        if opcion8 == 1:
            pass
    elif opcion == 6:
        exit()

if __name__ == "__main__":
    main()
