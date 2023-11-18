from tkinter import *
from GUI.estilos.style import *
from gestorAplicacion.Cliente import Cliente
from tkinter import messagebox
class ConsultarPlatoPreferido(Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background=BACKGROUND_CONTENEDOR)
        self._controlador = controlador
        
        self._inicializarTitulo()
        self._inicializarBoton()
        self._inicializarBoton()
        self._inicializarEtiquetaResultado()
        
    def _inicializarTitulo(self):    
        # Se inicializa el título  que va a estar en la parte superior de la ventana
        labelInicial = Label(self, justify=CENTER, text="Bienvenido al apartado de pedidos", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _inicializarBoton(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Pedido de envio", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _inicializarEtiquetaResultado(self):
        # Se inicializa la etiqueta para mostrar el resultado
        self._etiquetaResultado = Label(self, bg=BACKGROUND_CONTENEDOR, font=FONT2, fg="black")
        self._etiquetaResultado.pack(side=TOP, fill=BOTH, padx=10, pady=10)
    
    
        
    def _mostrarNombreYPlatoPreferido(self):
        # Se obtiene el id del cliente ingresado en la entrada
        idCliente = self._entradaId.get()
        
        # Se obtiene el nombre y plato preferido del cliente a partir del id
        try:
            nombreCliente = Cliente.buscarCliente(int(idCliente)).getNombre()
            platoPreferido = Cliente.buscarPlatoPreferido(int(idCliente))
        except:
            messagebox.showerror("Error", "El id ingresado no es válido o no hay suficientes facturas para calcular el plato preferido")
            return
        
        
        # Se muestra el resultado en la etiqueta correspondiente
        self._etiquetaResultado.configure(text=f"Nombre: {nombreCliente}\nPlato preferido: {platoPreferido}")
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
