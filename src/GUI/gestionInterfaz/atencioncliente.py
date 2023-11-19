from tkinter import *

class AtencionCliente(Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.configure(background="#72a18b")

        label1 = Label(self, text="Bienvenido al centro de Atencion al cliente\n¿Que desea realizar?", bg = "#a19f9f", font=("Roboto", 20), fg="#0a0a0a")
        label1.grid(row=0, column=2, columnspan=2, pady=10)

        botonSugerencia = Button(self, text="Sugerencia", command=self._mostrarNombreYPlatoPreferido, font=("Roboto", 12), fg="#0a0a0a")
        botonSugerencia.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonQueja = Button(self, text="Queja", command=self._mostrarNombreYPlatoPreferido, font=("Roboto", 12), fg="#0a0a0a")
        botonQueja.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonQueja = Button(self, text="Queja", command=self._mostrarNombreYPlatoPreferido, font=("Roboto", 12), fg="#0a0a0a")
        botonQueja.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonReseña = Button(self, text="Reseña", command=self._mostrarNombreYPlatoPreferido, font=("Roboto", 12), fg="#0a0a0a")
        botonReseña.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonDevolucion = Button(self, text="Devolución", command=self._mostrarNombreYPlatoPreferido, font=("Roboto", 12), fg="#0a0a0a")
        botonDevolucion.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    