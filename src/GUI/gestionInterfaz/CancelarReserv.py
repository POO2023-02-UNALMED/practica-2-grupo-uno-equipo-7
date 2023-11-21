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
from baseDatos import Deserializador,Serializador
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
        
        boton_reserva = tk.Button(self, text="Buscar", height=1, command=lambda: self.buscarReserva(self._entradaId.get()))
        boton_reserva.pack(pady=20)
        
        
    def buscarReserva(self, id): 
        clienteId = self._entradaId.get()
        try:
            nombreCliente = Cliente.buscarCliente(int(clienteId)).getNombre()
            platoPreferido = Cliente.buscarPlatoPreferido(int(clienteId))
        except:
            messagebox.showerror("Error", "El id ingresado no es válido")
            return
        
        reservasCliente = []
        
        for reserva in Reserva.listaReservas:

            if (int(reserva.getCliente().getId()) == int(id)):
                 reservasCliente.append(reserva)
                
        
        self.mostrarReserva(reservasCliente)

    def mostrarReserva(self, reservas):

        
        # Se inicializa el desplegable para mostrar las reservaciones
        self._desplegable = Combobox(self, state="readonly", font=FONT2)
        self._desplegable.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        self._desplegable.configure(values=reservas)
        self._desplegable.set("Seleccione su reservación")
        boton_cancelar = tk.Button(self, text="Eliminar", height=1, command=lambda: self.eliminar_reserva(self._desplegable.get()))
        boton_cancelar.pack(pady=20)

        
    def eliminar_reserva(self, reservaEliminada):
        for reserva in Reserva.listaReservas:
            if (reserva.__str__() == reservaEliminada):
                Reserva.listaReservas.remove(reserva)
                messagebox.showinfo( "Información","Su reserva ha sido cancelada")