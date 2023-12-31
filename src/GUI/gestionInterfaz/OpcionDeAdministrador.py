from tkinter import *
from GUI.estilos.style import *
from gestorAplicacion.Cliente import Cliente
from .consultarPlatoPreferido import ConsultarPlatoPreferido
from tkinter.ttk import Combobox
from tkinter import messagebox

class OpcionDeAdministrador(Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background=BACKGROUND_CONTENEDOR)
        self._controlador = controlador
        self._inicializarTitulo()
        self._inicializarEntrada()
        self._inicializarBoton()
        self._inicializarEtiquetaResultado()
        self._inicializarDesplegable()

     
        
    def _inicializarTitulo(self):    
        # Se inicializa el título  que va a estar en la parte superior de la ventana
        labelInicial = Label(self, justify=CENTER, text="Opciones de administrador", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _inicializarEntrada(self):
        # Se inicializa el frame para contener la etiqueta y la entrada
        frameEntrada = Frame(self, bg=BACKGROUND_CONTENEDOR)
        frameEntrada.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        # Se inicializa la etiqueta para el id del cliente
        labelId = Label(frameEntrada, text="Usuario", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        labelId.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Se inicializa la entrada para el id del cliente
        self._entradaId = Entry(frameEntrada, font=FONT2)
        self._entradaId.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
    def _inicializarBoton(self):
        # Se inicializa el botón para mostrar los platos recomendados para el cliente
        botonMostrar = Button(self, text="Continuar", command=self._mostrarPlatosRecomendados, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    