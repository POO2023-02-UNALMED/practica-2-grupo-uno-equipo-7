import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.inventarioaply import Inventarioaply
from gestorAplicacion.Restaurante import Restaurante
from gestorAplicacion.Mesa import *
from gestorAplicacion.Reserva import *
from GUI.estilos.style import *
from tkinter import *
from gestorAplicacion.Cliente import *
from tkinter.ttk import Combobox
class CancelarReserv(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background="white")
        self._controlador = controlador
        
        self._inicializarTitulo()
        self._inicializarEntrada()
        
    def _inicializarTitulo(self):    
        # Se inicializa el título  que va a estar en la parte superior de la ventana
        labelInicial = Label(self, justify=CENTER, text="Cancelar Reservación", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
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
        
        
        # Nombre
        frameEntrada1 = Frame(self, bg=BACKGROUND_CONTENEDOR)
        frameEntrada1.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        # Se inicializa la etiqueta para el id del cliente
        labelnm = Label(frameEntrada1, text="Nombre del cliente", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        labelnm.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Se inicializa la entrada para el id del cliente
        self._entradanm = Entry(frameEntrada1, font=FONT2)
        self._entradanm.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        boton_reserva = tk.Button(self, text="Buscar", height=1, command=lambda: self.buscarReserva(self._entradaId.get(), self._entradanm.get()))
        boton_reserva.pack(pady=20)
        
        
    def buscarReserva(self, id, nombre): 
        
        reservasCliente = []
        
        for reserva in Reserva.listaReservas:

            if (reserva.getCliente().getId() == int(id)):
                reservasCliente.append(reserva)
                
        
        self.mostrarReserva(reservasCliente)

    def mostrarReserva(self, reservas):
        
        # Se inicializa el desplegable para mostrar los platos recomendados para el cliente
        self._desplegable = Combobox(self, state="readonly", font=FONT2)
        self._desplegable.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        self._desplegable.configure(values=reservas)
        self._desplegable.set("Seleccione su reservación")
        self._desplegable.bind("<<ComboboxSelected>>", lambda event: self.eliminar_reserva(self._desplegable.get()))  
        
    def eliminar_reserva(self, reservaEliminada):
        print(len(Reserva.listaReservas))
        
        Reserva.listaReservas.remove(reservaEliminada)
        boton_cancelar = tk.Button(self, text="cancelar", height=1, command=lambda: self.buscarReserva(self._entradaId.get(), self._entradanm.get()))
        boton_cancelar.pack(pady=20)
        
        
        print(len(Reserva.listaReservas))