from tkinter import *
from GUI.estilos.style import *
from gestorAplicacion.Cliente import Cliente
from .consultarPlatoPreferido import ConsultarPlatoPreferido

class ConsultarPlatoRecomendado(Frame):
    
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
        labelInicial = Label(self, justify=CENTER, text="Consultar Plato Recomendado", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _inicializarEntrada(self):
        # Se inicializa el frame para contener la etiqueta y la entrada
        frameEntrada = Frame(self, bg=BACKGROUND_CONTENEDOR)
        frameEntrada.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        # Se inicializa la etiqueta para el id del cliente
        labelId = Label(frameEntrada, text="Id del cliente", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        labelId.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Se inicializa la entrada para el id del cliente
        self._entradaId = Entry(frameEntrada, font=FONT2)
        self._entradaId.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
    def _inicializarBoton(self):
        # Se inicializa el botón para mostrar los platos recomendados para el cliente
        botonMostrar = Button(self, text="Mostrar", command=self._mostrarPlatosRecomendados, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _inicializarEtiquetaResultado(self):
        # Se inicializa la etiqueta para mostrar el resultado
        self._etiquetaResultado = Label(self, bg=BACKGROUND_CONTENEDOR, font=FONT2, fg="black")
        self._etiquetaResultado.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _mostrarPlatosRecomendados(self):
        # Se obtiene el id del cliente ingresado en la entrada
        idCliente = self._entradaId.get()
        
        # Se obtienen los platos recomendados para el cliente a partir del id
        platosRecomendados = Cliente.buscarPlatoRecomendado(int(idCliente))
        nombreCliente = Cliente.buscarCliente(int(idCliente)).getNombre()
        platoPreferido = Cliente.buscarPlatoPreferido(int(idCliente))
        
        
        # Se muestra el resultado en la etiqueta correspondiente
        
        
        
        # Se muestra el resultado en la etiqueta correspondiente
        resultado = "Platos recomendados:\n"
        for i, plato in enumerate(platosRecomendados):
            resultado += f"{i+1}. {plato.nombre}\n"
        self._etiquetaResultado.configure(text=resultado)
        self._etiquetaResultado.configure(text=f"Nombre: {nombreCliente}\nPlato preferido: {platoPreferido}\n{resultado}")
