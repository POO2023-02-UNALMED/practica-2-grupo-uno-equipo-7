from GUI.gestionInterfaz.inicio import Inicio
from tkinter import *
from GUI.estilos import style






class Manager(Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inicio")
        self.option_add('*tearOff', False)
        contenedor = Frame(self)
        contenedor.pack(side = TOP, fill = BOTH, expand = True)
        contenedor.configure(background = style.BACKGROUND_CONTENEDOR)
        contenedor.grid_columnconfigure(0, weight = 1)
        contenedor.grid_rowconfigure(0, weight = 1)
        
        self._ventanaInicio = Inicio(contenedor, self)
        self._ventanaInicio.grid(row = 0, column = 0, sticky = NSEW)