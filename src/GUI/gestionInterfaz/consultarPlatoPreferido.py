from tkinter import *
from GUI.estilos.style import *

class ConsultarPlatoPreferido(Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background=BACKGROUND_CONTENEDOR)
        self._controlador = controlador
        
        self._inicializarTitulo()
        self._inicializarEntrada()
        self._inicializarBoton()
        self._inicializarEtiquetaResultado()
        
    def _inicializarTitulo(self):    
        # Se inicializa el título  que va a estar en la parte superior de la ventana
        labelInicial = Label(self, justify=CENTER, text="Consultar Plato Preferido", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _inicializarEntrada(self):
        # Se inicializa la entrada para el id del cliente
        self._entradaId = Entry(self, font=FONT2)
        self._entradaId.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _inicializarBoton(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Mostrar", command=self._mostrarNombreYPlatoPreferido, font=FONT2, fg=FG)
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _inicializarEtiquetaResultado(self):
        # Se inicializa la etiqueta para mostrar el resultado
        self._etiquetaResultado = Label(self, bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        self._etiquetaResultado.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _mostrarNombreYPlatoPreferido(self):
        # Se obtiene el id del cliente ingresado en la entrada
        idCliente = self._entradaId.get()
        
        # Se obtiene el nombre y plato preferido del cliente a partir del id
        nombreCliente = self._controlador.obtenerNombreCliente(idCliente)
        platoPreferido = self._controlador.obtenerPlatoPreferidoCliente(idCliente)
        
        # Se muestra el resultado en la etiqueta correspondiente
        self._etiquetaResultado.configure(text=f"Nombre: {nombreCliente}\nPlato preferido: {platoPreferido}")
