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
        labelInicial = Label(self, justify=CENTER, text="Bienvenido al apartado de Pedido Fisico", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)


        
    def _EntradaNombre(self):
        # Se inicializa el frame para contener la etiqueta y la entrada
        frameEntrada = Frame(self, bg=BACKGROUND_CONTENEDOR)
        frameEntrada.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        # Se inicializa la etiqueta para el id del cliente
        labelNombre = Label(frameEntrada, text="Nombre", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        labelNombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Se inicializa la entrada para el id del cliente
        self._entradaNombre = Entry(frameEntrada, font=FONT2)
        self._entradaNombre.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def _EntradaIden(self):
        # Se inicializa el frame para contener la etiqueta y la entrada
        frameEntrada = Frame(self, bg=BACKGROUND_CONTENEDOR)
        frameEntrada.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        # Se inicializa la etiqueta para el id del cliente
        labelIden = Label(frameEntrada, text="Identificación", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        labelIden.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Se inicializa la entrada para el id del cliente
        self._entradaIden = Entry(frameEntrada, font=FONT2)
        self._entradaIden.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def _EntradaDireccion(self):
        # Se inicializa el frame para contener la etiqueta y la entrada
        frameEntrada = Frame(self, bg=BACKGROUND_CONTENEDOR)
        frameEntrada.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        # Se inicializa la etiqueta para el id del cliente
        labelDirection = Label(frameEntrada, text="Dirección", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        labelDirection.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Se inicializa la entrada para el id del cliente
        self._entradaDirection = Entry(frameEntrada, font=FONT2)
        self._entradaDirection.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
    def _BotonContinuar(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonContinuar = Button(self, text="Continuar", command=self._confirPedidoEnvio, font=FONT2, fg="green")
        botonContinuar.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _confirPedidoEnvio(self):
        LabelConfir = Label(self, justify=CENTER, text=f"Los datos ingresados son nombre: {self._EntradaNombre}, Identificación: {self._EntradaIden} y Dirección: {self._entradaDirection}. Desea confirmar estos datos? ", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        LabelConfir.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonConfirN = Button(self, text="No confirmar", command=self._BotonContinuar, font=FONT2, fg="green")
        botonConfirN.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonConfirS = Button(self, text="Confirmar", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonConfirS.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
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
