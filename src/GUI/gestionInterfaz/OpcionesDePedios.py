from tkinter import *
from GUI.estilos.style import *
from gestorAplicacion.Cliente import Pedido
from tkinter import messagebox
class ConsultarPlatoPreferido(Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background=BACKGROUND_CONTENEDOR)
        self._controlador = controlador
        
        self._inicializarTitulo()
        self._Boton1()
        self._Boton2()
        self._Boton3()
        self._Boton4()
        
        
    def _inicializarTitulo(self):    
        # Se inicializa el título  que va a estar en la parte superior de la ventana
        labelInicial = Label(self, justify=CENTER, text="Bienvenido al apartado de pedidos", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _Boton1(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Pedido de envio", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _Boton2(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Pedido Fisico", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _Boton3(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Opciones de administrador", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _Boton4(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Volver al inicio", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    

