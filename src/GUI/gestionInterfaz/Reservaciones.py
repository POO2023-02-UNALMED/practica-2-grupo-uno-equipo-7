from tkinter import *
from GUI.estilos.style import *
from gestorAplicacion.Cliente import *
from tkinter import messagebox
from gestorAplicacion.Mesa import *
from gestorAplicacion.Reserva import *


class Reservaciones(Frame):

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background=BACKGROUND_CONTENEDOR)
        self._controlador = controlador

        self._inicializarTitulo()
        self._inicializarFecha()
        self._inicializarBoton()
        self._inicializarEtiquetaResultado()

    def _inicializarTitulo(self):
        # Se inicializa el título  que va a estar en la parte superior de la ventana
        labelInicial = Label(self, justify=CENTER, text="Generar Reservaciones",
                             bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _inicializarFecha(self):
        pass
