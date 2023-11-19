from tkinter import *

class AtencionCliente(Frame):

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self._controlador = controlador
        self.configure(background="#72a18b")

        self._mostrarTitulo()
        self._botonSugerencia()
        self._botonQueja()
        self._botonReseña()
        self._botonDevolucion()

    def _mostrarTitulo(self):
        label1 = Label(self, text="Bienvenido al centro de Atencion al cliente\n¿Que desea realizar?", bg="#a19f9f", font=("Roboto", 20), fg="#0a0a0a")
        label1.pack(side=TOP, fill=BOTH, expand=True, pady=10)

    def _botonSugerencia(self):
        botonSugerencia = Button(self, text="Sugerencia", command=self.mostrar, font=("Roboto", 12), fg="#0a0a0a")
        botonSugerencia.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _botonQueja(self):
        botonQueja = Button(self, text="Queja", command=self.mostrar, font=("Roboto", 12), fg="#0a0a0a")
        botonQueja.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _botonReseña(self):
        botonReseña = Button(self, text="Reseña", command=self.mostrar, font=("Roboto", 12), fg="#0a0a0a")
        botonReseña.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _botonDevolucion(self):
        botonDevolucion = Button(self, text="Devolución", command=self.mostrar, font=("Roboto", 12), fg="#0a0a0a")
        botonDevolucion.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def mostrar(self):
        print("Prueba")

    