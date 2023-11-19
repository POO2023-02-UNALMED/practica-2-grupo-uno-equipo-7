from tkinter import *
import tkinter as tk
from GUI.estilos.style import *

class Atencion_Cliente(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.configure(background="#72a18b")
        self._inicializarTitulo()
        self._Boton1()
        self._Boton2()
        self._Boton3()
        self._Boton4()
        self._Boton5()
        
    def _inicializarTitulo(self):    
        # Se inicializa el título  que va a estar en la parte superior de la ventana
        label1 = tk.Label(self, text="Bienvenido al centro de Atencion al cliente\n¿Que desea realizar?", bg = "#a19f9f", font=("Roboto", 20), fg="#0a0a0a")
        label1.grid(row=0, column=2, columnspan=2, pady=10)

    def _Boton1(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Sugerencia", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _Boton2(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Queja", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _Boton3(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Reseña", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _Boton4(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Devolución", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)
    
    def _Boton5(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Volver al inicio", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)