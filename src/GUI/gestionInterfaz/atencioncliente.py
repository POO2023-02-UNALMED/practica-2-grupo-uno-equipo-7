from tkinter import *
from gestorAplicacion.Sugerencia import Sugerencia

class NuevaSugerencia(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Nueva Sugerencia")

        # Etiqueta y menú desplegable
        label_tipo = Label(self, text="Tipo:")
        label_tipo.pack(side=TOP, pady=5)

        opciones_tipo = ["Menu", "Empleado", "Sedes", "Otros"]
        self.var_tipo = StringVar(self)
        self.var_tipo.set(opciones_tipo[0])  # Establecer el valor predeterminado
        menu_tipo = OptionMenu(self, self.var_tipo, *opciones_tipo)
        menu_tipo.pack(side=TOP, pady=5)

        # Etiqueta y entrada para la sugerencia
        label_sugerencia = Label(self, text="Sugerencia:")
        label_sugerencia.pack(side=TOP, pady=5)

        self.entry_sugerencia = Entry(self, width=30)
        self.entry_sugerencia.pack(side=TOP, pady=5)

        # Botón para guardar la sugerencia
        boton_guardar = Button(self, text="Guardar", command=self.guardar_sugerencia)
        boton_guardar.pack(side=TOP, pady=10)

    def guardar_sugerencia(self):
        tipo = self.var_tipo.get()
        sugerencia = self.entry_sugerencia.get()

        sug = Sugerencia(tipo,sugerencia)
        
        print(sug)

class VentanaSugerencia(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones de Sugerencia")

        boton_crear_sugerencia = Button(self, text="Crear nueva sugerencia", command=self.crear_nueva_sugerencia, font=("Roboto", 12), fg="#0a0a0a")
        boton_crear_sugerencia.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        boton_reportes = Button(self, text="Reportes", command=self.mostrar_reportes, font=("Roboto", 12), fg="#0a0a0a")
        boton_reportes.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def crear_nueva_sugerencia(self):
        ventana_nueva_sugerencia = NuevaSugerencia(self)

    def mostrar_reportes(self):
        print("Mostrar reportes")

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
        label1.pack(side=TOP, fill=BOTH, pady=10)

    def _botonSugerencia(self):
        botonSugerencia = Button(self, text="Sugerencia", command=self._crear_ventana_sugerencia, font=("Roboto", 12), fg="#0a0a0a")
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

    def _crear_ventana_sugerencia(self):
        ventana_sugerencia = VentanaSugerencia(self)

    def mostrar(self):
        print("Prueba")

    