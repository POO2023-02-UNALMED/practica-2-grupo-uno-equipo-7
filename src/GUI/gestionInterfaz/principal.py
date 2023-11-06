# Se importan las librerías que vamos a utilizar
from tkinter import *
from GUI.gestionInterfaz.reporte import Reporte
from GUI.Menu.menuPrincipal import MenuPrincipal
from GUI.estilos.style import *


class Principal(Toplevel):
    
    # Se crea el contructor de la clase
    def __init__(self, padre):
        # Se llama al padre (Toplevel)
        super().__init__(padre)
        
        # Titulo
        self.title("Mascotas UN")
        self.geometry("1280x1080")
        # Se agrega el menu
        menuPrincipal = MenuPrincipal(self, padre)
        self['menu'] = menuPrincipal
        
        # Inicio
        self._contenedor = Frame(self)
        self._contenedor.pack(side=TOP, fill=BOTH, expand=True)
        self._contenedor.configure(background=BACKGROUND_CONTENEDOR)
        self._contenedor.grid_columnconfigure(0, weight=1)
        self._contenedor.grid_rowconfigure(0, weight=1)
        
        self.frameFuncionalidad = {}
        