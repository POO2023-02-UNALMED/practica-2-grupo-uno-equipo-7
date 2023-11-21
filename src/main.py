from datetime import date
from enum import Enum

from gestorAplicacion.Cliente import Cliente
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Restaurante import Restaurante
from gestorAplicacion.Plato import Plato
from gestorAplicacion.Factura import Factura

from gestorAplicacion.Sugerencia import Sugerencia
from gestorAplicacion.Queja import Queja
from gestorAplicacion.Reseña import Reseña
from gestorAplicacion.Devolucion import Devolucion


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
        
        print("Bienvenid@ al sistema de atención al cliente.\n¿Que desea realizar?")

        print("1. Salir")
        print("2. Sugerencia")
        print("3. Queja")
        print("4. Reseña")
        print("5. Devolucion")

        opcionAC = int(input("Elija una opcion: "))

        if opcionAC == 2: #Sugerencia
            print("------------Sugerencias------------")
            print("Ha seleccionado la opcion 1, Sugerencia,\n¿Que desea realizar?")

            print("1. Realizar una nueva sugerencia")
            print("2. Reporte de sugerencias")
            print("3. Volver") #¿Salir?

            opcionSugerencia = int(input("Elija una opcion: "))

            if opcionSugerencia == 1:
                print("¿Sobre que desea realizar su sugerecia?")
                print("1. Sobre el menu")
                print("2. Sobre un empleado")
                print("3. Sobre una de nuestras sedes")
                print("4. Algun otro")
                print("5. Volver") #¿Salir?

                opcionSType = int(input("Elija una opcion: "))
                STipo = "Otro"

                if opcionSType == 1:
                    STipo = "Menu"
                
                elif opcionSType == 2:
                    STipo = "Empleado"

                elif opcionSType == 3:
                    STipo = "Sede"
                
                elif opcionSType == 4:
                    STipo = "Otro"
                
                elif opcionSType > 5 or opcionSType < 1:
                    print("Opción invalida")
                
                #else:
                    #print("Saliendo") #¿Salir?
                
                if opcionSType >= 1 or opcionSType <= 5:

                    STexto = str(input("Por favor, a continuacion escriba su sugerencia"))

                    print("Todo listo")
                    print("1. Editar Sugerencia")
                    print("2. Enviar Sugerencia")

                    opcionES = int(input("Elija una opcion: "))

                    if opcionES == 1:
                        editado = str(input("Ahora puede editar su sugerencia: "))
                        STexto = editado
                        print("Todo listo, enviando sugerencia ...")
                    
                    else:
                        print("Enviando sugerencia ...")

                    sugerencia = Sugerencia(STipo, STexto)
                    
                    print("Su sugerencia se ha enviado con exito")

                    print("\n")
                    print(sugerencia)
                    print("\n")

                    #print("Saliendo") #¿salir?

            elif opcionSugerencia == 2: #Reportes de sugerencias
                print("Para poder continuar debe ingresar su codigo de empleado. ¿Cuenta con un codigo de empelado?")

                print("1. Si")
                print("2. No")

                opcionSEmpleado = int(input("Elija una opcion: "))

                if opcionSEmpleado == 2:

                    print("Lo siento, tiene que tener un codigo de empleado para poder ingresar")
                    #print("saliendo ...") #¿Salir?
                
                else:
                    codigoES = int(input("Ingrese su codigo de empleado: "))

                    verificandoEmpleado = Empleado.buscarEmpleadoXCodigo(codigoES)

                    if verificandoEmpleado == None:
                        print("El codigo es invalido")
                        #print("Saliendo") #¿Saliendo?
                    
                    else:
                        print("Bienvenid@ " + verificandoEmpleado.getNombre() + "\n¿Que reporte desea que le muestre?")

                        print("1. Reporte de todas las sugerencias")
                        print("2. Reporte de sugerencias del menu")
                        print("3. Reporte de sugerencias sobre empleados")
                        print("4. Reporte de sugerencias de sede")
                        print("5. Volver")  #¿Salir?

                        Sugerencias = Sugerencia.getTAllSugerences()
                        SugerenciasM = Sugerencia.getSugerenciasMenu()
                        SugerenciasE = Sugerencia.getSugerenciasEmpleados()
                        SugerenciasS = Sugerencia.getSugerenciasSedes()
                        SugerenciasO = Sugerencia.getSugerenciasOtros()

                        opcionReportesSugerencias = int(input("Elija una opcion: "))

                        if opcionReportesSugerencias == 1: #Reporte de todas las sugerencias
                            
                            countS = Sugerencia.cantidadSugerencias()
                            print(countS)

                            if countS != "No hay sugerencias que mostrar":

                                print("¿Desea ver c/u de las sugerencias mencionadas?")

                                print("1. Si")
                                print("2. No")

                                reporteAllS = int(input("Elija una opcion: "))

                                if reporteAllS == 2:
                                    pass
                                    #print("Saliendo ...") #Salir?
                                
                                else:

                                    for sug in Sugerencias:
                                        print("\n")
                                        print(sug)
                                        print("\n")

                        elif opcionReportesSugerencias == 2: #Reportes sugerencias Menu
                            
                            countSM = Sugerencia.cantidadSugerenciasMenu()
                            print(countSM)
                            
                            if countSM != "No hay sugerencias que mostrar":

                                print("¿Desea ver c/u de las sugerencias mencionadas?")

                                print("1. Si")
                                print("2. No")

                                reporteSM = int(input("Elija una opcion: "))

                                if reporteSM == 2:
                                    pass
                                    #print("Saliendo ...") #Salir?
                                
                                else:

                                    for sug in SugerenciasM:
                                        print("\n")
                                        print(sug)
                                        print("\n")
                        
                        elif opcionReportesSugerencias == 3: #Reportes sugerencias Empleados
                            
                            countSE = Sugerencia.cantidadSugerenciasEmpleados()
                            print(countSE)
                            
                            if countSE != "No hay sugerencias que mostrar":

                                print("¿Desea ver c/u de las sugerencias mencionadas?")

                                print("1. Si")
                                print("2. No")

                                reporteSE = int(input("Elija una opcion: "))

                                if reporteSE == 2:
                                    pass
                                    #print("Saliendo ...") #Salir?
                                
                                else:

                                    for sug in SugerenciasE:
                                        print("\n")
                                        print(sug)
                                        print("\n")
                        
                        elif opcionReportesSugerencias == 4: #Reportes sugerencias Sede
                            
                            countSS = Sugerencia.cantidadSugerenciasSedes()
                            print(countSS)
                            
                            if countSS != "No hay sugerencias que mostrar":

                                print("¿Desea ver c/u de las sugerencias mencionadas?")

                                print("1. Si")
                                print("2. No")

                                reporteSS = int(input("Elija una opcion: "))

                                if reporteSS == 2:
                                    pass
                                    #print("Saliendo ...") #Salir?
                                
                                else:

                                    for sug in SugerenciasS:
                                        print("\n")
                                        print(sug)
                                        print("\n")
                        
                        elif opcionReportesSugerencias == 5: #Reportes sugerencias Otros
                            
                            countSO = Sugerencia.cantidadSugerenciasOtros()
                            print(countSO)
                            
                            if countSO != "No hay sugerencias que mostrar":

                                print("¿Desea ver c/u de las sugerencias mencionadas?")

                                print("1. Si")
                                print("2. No")

                                reporteSO = int(input("Elija una opcion: "))

                                if reporteSO == 2:
                                    pass
                                    #print("Saliendo ...") #Salir?
                                
                                else:

                                    for sug in SugerenciasO:
                                        print("\n")
                                        print(sug)
                                        print("\n")
                        
                        else:
                            pass
                            #print("Saliendo ...") #¿Salir?
            
            else: #fin de sugerencias
                #print("Saliendo ...") #¿Salir?
                pass

        elif opcionAC == 3: #Queja
            print("------------Quejas------------")
            print("Ha seleccionado la opcion 2, Quejas\n¿Que desea realizar?")
			
            print("1. Realizar una nueva queja")
            print("2. Reporte de quejas")
            print("3. Salir")

            opcionQuejas = int(input("Elija una opcion: "))

            if opcionQuejas == 2: #Nueva Queja

                Qnombre = str(input("Por favor, a continuacion ingrese su nombre completo: "))
                print("¿Sobre que desea realizar su queja?")
				
                print("1. Sobre el menu")
                print("2. Sobre un empleado")
                print("3. Sobre una de nuestras sedes")
                print("4. Algun otro")
                print("5. Salir")

                opcionQType = int(input("Elija una opcion: "))
                QTipo = "Otro"
                QOtro = None

                if opcionQType == 1:
                    QTipo = "Menu"

                    print("Para poder continuar debe ingresar el nombre del plato del cual desea quejarse. ¿Cuenta con el nombre del plato?")
                    print("1. Si")
                    print("2. No")

                    opcionQP = int(input("Elija una opcion: "))

                    if opcionQP == 1: #Si tiene el nombre del plato

                        nombreP= str(input("Ingrese el nombre del plato: "))

                        verificandoPlatoQ = Plato.buscarPlato()

                        if verificandoPlatoQ == None:
                            print("Este plato no existe")
                        
                        else:
                            QOtro = nombreP
                    else: #No trae eñ nombre del plato
                        print("Sin el nombre del plato no es posible realizar una queja especifica, le recomendamos escribir su queja en ''Algun Otro''")
                        #print("Saliendo ...") #¿Salir?
                        pass

                elif opcionQType == 2:
                    QTipo = "Empleado"

                    print("Para poder continuar debe ingresar el nombre del empleado del cual desea quejarse. ¿Cuenta con el nombre del empleado?")
                    print("1. Si")
                    print("2. No")

                    opcionQE = int(input("Elija una opcion: "))

                    if opcionQE == 1: #Si tiene el nombre del empleado

                        nombreEQ= str(input("Ingrese el nombre del plato: "))

                        verificandoEmpleadoQ = Empleado.buscarEmpleadoXNombre()

                        if verificandoEmpleadoQ == None:
                            print("Este empleado no existe")
                        
                        else:
                            QOtro = nombreEQ
                    else: #No trae eñ nombre del Empleado
                        print("Sin el nombre del empleado no es posible realizar una queja especifica, le recomendamos escribir su queja en ''Algun Otro''")
                        #print("Saliendo ...") #¿Salir?
                        pass

                elif opcionQType == 3:
                    QTipo = "Sede"

                    print("Por favor, para continuar indique la sede de la cual quiere hacer su queja")
					
                    print("1. Sede La America")
                    print("2. Sede Sandiego")
                    print("3. Sede Envigado")
                    print("4. Sede Belen")

                    SedeQ = int(input("Elija una opcion: "))

                    if SedeQ == 1:
                        QOtro = "Sede: La America"
                    elif SedeQ == 2:
                        QOtro = "Sede: Sandiego"
                    elif SedeQ == 3:
                        QOtro = "Sede: Envigado"
                    elif SedeQ == 4:
                        QOtro = "Sede: Belen"
                    else:
                        print("Esta sede no existe")
    
                elif opcionQType == 4:
                    QTipo = "Otro"
                    QOtro = None
                
                elif opcionQType > 5 or opcionQType < 1:
                    print("Opción invalida")
                
                else:
                    pass
                    #print("Saliendo") #¿Salir?

                if opcionQType >= 1 or opcionQType <= 5:
                    QTexto = str(input("Por favor, a continuacion escriba su queja: "))

                    print("Todo listo")
                    print("1. Editar Queja")
                    print("2. Enviar Queja")

                    opcionEQ = int(input("Elija una opcion: "))

                    if opcionEQ == 1:
                        editadoQ = str(input("Ahora puede editar su queja: "))
                        QTexto = editadoQ
                        print("Todo listo, enviando queja ...")
                    
                    else:
                        print("Enviando queja ...")

                    queja = Queja(Qnombre,QTipo, QOtro, QTexto)
                    
                    print("Su queja se ha enviado con exito")

                    print("\n")
                    print(queja)
                    print("\n")

                
            elif opcionQuejas == 3: #Reporte Quejas
                print("Para poder continuar debe ingresar su codigo de empleado. ¿Cuenta con un codigo de empelado?")

                print("1. Si")
                print("2. No")

                opcionQEmpleado = int(input("Elija una opcion: "))

                if opcionQEmpleado == 2:

                    print("Lo siento, tiene que tener un codigo de empleado para poder ingresar")
                    #print("saliendo ...") #¿Salir?
                    pass
                
                else:
                    codigoEQ = int(input("Ingrese su codigo de empleado: "))

                    verificandoEmpleadoQI = Empleado.buscarEmpleadoXCodigo(codigoEQ)

                    if verificandoEmpleadoQI == None:
                        print("El codigo es invalido")
                        #print("Saliendo") #¿Saliendo?
                    
                    else:
                        print("Bienvenid@ " + verificandoEmpleadoQI.getNombre() + "\n¿Que reporte desea que le muestre?")

                        print("1. Reporte de todas las quejas")
                        print("2. Reporte de quejas del menu")
                        print("3. Reporte de quejas sobre empleados")
                        print("4. Reporte de quejas de sede")
                        print("5. Reporte de quejas otros")
                        print("6. Volver")  #¿Salir?

                        Quejas = Queja.getTAllQuejas()
                        QuejasM = Queja.getQuejasMenu()
                        QuejasE = Queja.getQuejasEmpleados()
                        QuejasS = Queja.getQuejasSedes()
                        QuejasO = Queja.getQuejasOtros()

                        opcionReportesQuejas = int(input("Elija una opcion: "))

                        if opcionReportesQuejas == 1: #Reporte de todas las quejas
                            
                            countQ = Quejas.cantidadQuejas()
                            print(countQ)

                            if countQ != "No hay quejas que mostrar":

                                print("¿Desea ver c/u de las quejas mencionadas?")

                                print("1. Si")
                                print("2. No")

                                reporteAllQ = int(input("Elija una opcion: "))

                                if reporteAllQ == 2:
                                    pass
                                    #print("Saliendo ...") #Salir?
                                
                                else:

                                    for que in Quejas:
                                        print("\n")
                                        print(que)
                                        print("\n")

                        elif opcionReportesQuejas == 2: #Reportes quejas Menu
                            
                            countQM = Queja.cantidadQuejasMenu()
                            print(countQM)
                            
                            if countQM != "No hay quejas que mostrar":

                                print("¿Desea ver c/u de las quejas mencionadas?")

                                print("1. Si")
                                print("2. No")

                                reporteQM = int(input("Elija una opcion: "))

                                if reporteQM == 2:
                                    #print("Saliendo ...") #Salir?
                                    pass
                                
                                else:

                                    for que in  QuejasM:
                                        print("\n")
                                        print(que)
                                        print("\n")
                        
                        elif opcionReportesQuejas == 3: #Reportes quejas Empleados
                            
                            countQE = Queja.cantidadQuejasEmpleados()
                            print(countQE)
                            
                            if countQE != "No hay quejas que mostrar":

                                print("¿Desea ver c/u de las quejas mencionadas?")

                                print("1. Si")
                                print("2. No")

                                reporteQE = int(input("Elija una opcion: "))

                                if reporteQE == 2:
                                    pass
                                    #print("Saliendo ...") #Salir?
                                
                                else:

                                    for que in QuejasE:
                                        print("\n")
                                        print(que)
                                        print("\n")
                        
                        elif opcionReportesQuejas == 4: #Reportes quejas Sede
                            
                            countQS = Queja.cantidadQuejasSedes()
                            print(countQS)
                            
                            if countQS != "No hay quejas que mostrar":

                                print("¿Desea ver c/u de las quejas mencionadas?")

                                print("1. Si")
                                print("2. No")

                                reporteQS = int(input("Elija una opcion: "))

                                if reporteQS == 2:
                                    pass
                                    #print("Saliendo ...") #Salir?
                                
                                else:

                                    for que in QuejasS:
                                        print("\n")
                                        print(que)
                                        print("\n")
                        
                        elif opcionReportesQuejas == 5: #Reportes quejas Otros
                            
                            countQO = Queja.cantidadQuejasOtros()
                            print(countQO)
                            
                            if countQO != "No hay quejas que mostrar":

                                print("¿Desea ver c/u de las quejas mencionadas?")

                                print("1. Si")
                                print("2. No")

                                reporteQO = int(input("Elija una opcion: "))

                                if reporteQO == 2:
                                    pass
                                    #print("Saliendo ...") #Salir?
                                
                                else:

                                    for que in QuejasO:
                                        print("\n")
                                        print(que)
                                        print("\n")

                        else:
                            #Salir
                            pass    
            else:
                pass
                #print("Saliendo ...") #¿Salir?
			

        elif opcionAC == 3: #Reseña
            print("------------Reseñas------------")
            print("Ha seleccionado la opcion 3, Reseña.\n¿Que desea realizar?")
			
            print("1. Ver repositorio de reseñas")
            print("2. Realizar una nueva reseña")
            print("3. Reporte de calificaiones")
            print("4. Salir")

            opcionReseña = int(input("Elija una opcion"))
            Reseñas = Reseña.getRecopilatorio()

            if opcionReseña == 1: #Ver repositorio
               
                print("Mostrando recopilatorio de reseñas ...")

                for rsñ in Reseñas:
                    print(rsñ)
                    print("\n")

            elif opcionReseña == 2: #Realizar nueva reseña
                RNombre = "Anonimo"
                print("¿Desea que la reseña sea anonima?")
                print("1. Si")
                print("2. No")

                nombreR = int(input("Elija una opción"))

                if nombreR == 2:
                    name = str(input("Por favor, ingrese su nombre completo: "))

                    RNombre = name
                
                else:
                    RNombre = "Anonimo"
                
                RTexto = str(input("Por favor, escriba su reseña: "))
                RCalificacion = str(input("Por favor, indique del 1-5 que calificación le daria a su experiencia en el restaurante, donde 1 es mul mal y 5 muy bien: "))

                print("¿Desea editar su reseña?")
                print("1. Si")
                print("2. No")

                editarReseña = int(input("Elija una opcion: "))

                if editarReseña == 1:
                    editando = str(input("Ahora puede editar su reseña"))
                    RTexto = editando
                    print("¿Desea editar tambien su calificacion?")
                    print("1. Si")
                    print("2. No")

                    editarCalificacion = int(input("Elija una opcion: "))
                    if editarCalificacion == 1:
                        editandoC = int(input("Ahora puede editar su calificacion: "))
                        RCalificacion = editandoC

                reseña = Reseña(RNombre, RTexto, RCalificacion)
                print("Todo listo, su reseña se esta enviando ...")
                print("Su reseña se ha enviado con exito")

                print("\n")
                print(reseña)
                print("\n")

                print("1. Salir")
                print("2. Ver repositorio de reseñas")

                finNuevaReseña = int(input("Elija una opcion: "))

                if finNuevaReseña == 2:
                    print("Mostrando recopilatorio de reseñas ...")

                for rsña in Reseñas:
                    print(rsña)
                    print("\n")
                
                else: pass

            elif opcionReseña == 3: #Reporte calificaciones
                print(Queja.PromedioCalificaciones())
                print("\n")
                #print("Saliendo ...") #¿Salir?
                pass

            else: pass

        elif opcionAC == 4: #Devolucion
            print("------------Devoluciones------------")
            print("Ha seleccionado la opcion 4, Devoluciones.\n¿Que desea realizar?")
			
            print("1. Ver las solicitudes de Devoluciones")
            print("2. Realizar una nueva solicitud")
            print("3. Revisar el estado de mi solicitud")
            print("4. Salir")

            opcionDevolucion = int(input("Elija una opcion: "))
            Devoluciones = Devolucion.getDevoluciones()

            if opcionDevolucion == 1: #Ver las solicitudes
                print("Para poder continuar debe ingresar su codigo de empleado. ¿Cuenta con un codigo de empelado?")

                print("1. Si")
                print("2. No")

                opcionDEmpleado = int(input("Elija una opcion: "))

                if opcionDEmpleado == 2:

                    print("Lo siento, tiene que tener un codigo de empleado para poder ingresar")
                    pass
                    #print("saliendo ...") #¿Salir?
                
                else:
                    codigoED = int(input("Ingrese su codigo de empleado: "))

                    verificandoEmpleadoD = Empleado.buscarEmpleadoXCodigo(codigoED)

                    if verificandoEmpleadoD == None:
                        print("El codigo es invalido")
                        #print("Saliendo") #¿Saliendo?
                        pass
                    
                    else:
                        print("Bienvenid@ " + verificandoEmpleadoD.getNombre() + "\nA continucion se mostraran todas las solicitudes pendientes")

                        for devolucion in Devoluciones:
                            print(devolucion)
                            print("\n")

                        print("¿Desea revisar y cambiar el estado de una solucitud?")
						
                        print("1. Si")
                        print("2. No/Salir")

                        revisarEstado = int(input("Elija una opcion: "))

                        if revisarEstado == 2:
                            pass
                        
                        else: 
                            codigoSolicitud = int(input("Por favor ingrese el numero de la solicitud que desea revisar: "))

                            solicitud = Devolucion.buscarDevolucion(codigoSolicitud)
                            
                            print("¿Desea aprobar o denegar la solicitud?")
							
                            print("1. Aprobar")
                            print("2. Denegar")

                            cambiarEstado = int(input("Elija una opcion: "))

                            if cambiarEstado == 1:
                                Devolucion.AprobarDevolucion(codigoSolicitud)
                                print("Todo listo, la solicitud fue aprobada con exito\n")

                            else:
                                razon = str(input("Para poder denegar la solicitud por favor indique la razon: "))
                                Devolucion.DenegarDevolucio(codigoSolicitud, razon)

                                print("Todo listo, la solicitud fue denegada con exito\n")

                            print(solicitud)
                            print("\nSaliendo")
                            pass
                    
            elif opcionDevolucion == 2: #Nueva solicitud
                print("Para realizar una nueva solicitud por favor ingrese los siguientes datos")

                nombreD = str(input("Ingresar Nombre completo: "))
                cedulaD = str(input("Ingresar Cedula: "))
                correoD = str(input("Ingresar Correo: "))
                facturaD = str(input("Ingresar el codigo de su factura: "))

                print("Por favor espere unos segundos mientras verificamos los datos")

                verificarFactura =  Factura.existeFactura(facturaD)

                if verificarFactura == False:

                    print("El numero de factura que ingreso no existe por lo tanto no es valido")
                
                else:
                    textoD = str(input("Sus datos son validos, por favor ingrese el motivo de su devolucion para continuar: "))

                    dlv = Devolucion(nombreD, cedulaD, correoD, facturaD, textoD)

                    print("Todo listo, su solicitud ha sido creada y enviada con exito,\nNos estaremos comunicando con usted proximamente con la debida respuesta a su solicitud")

                    print("\n")
                    print(dlv)
                pass

            elif opcionDevolucion == 3: #Revisar estado

                codigosol = int(input("Por favor ingrese el n° de la solicitud: "))
                devl = Devolucion.buscarDevolucion(codigosol)

                if devl == None:
                    print("Esta solicitud no existe")
                    #print("Saliendo ...")
                    pass

                else: 
                    print("Todo listo, mostando solicitud ... ")
                    print("\n")
                    print(devl)
                pass

            else: pass

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
                #ubicacion = Pedido.Direccion(direccion)
                print(f"Ha ingresado la dirección: {direccion}.")
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
                        
                    else: 
                        print("Productos seleccionados")
                        print("El total de su compra es: ")
                        #metodo para mostrar el total de la compra mas un adicional por el domicilio 
                        print("Confirmción final")
                        print("¿Desea confirmar su pedido?")
                        confirfinal = str(input())
                        if confirfinal == "N":
                            print("Pedido no confirmado, ¿desea volver al menu principal?")

                        else:
                            print("Pedido confirmado, Gracias por su compra, el total a pagar será cobrado al momento de recibir su pedido (Pago contra entrega)")
                            print("Vuelva pronto")
                    

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
    
