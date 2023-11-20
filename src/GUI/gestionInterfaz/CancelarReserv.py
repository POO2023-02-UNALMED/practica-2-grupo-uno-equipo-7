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
            if (reserva.getCliente().getId() == id):
                reservasCliente.append(reserva)
        
        self.mostrarReserva(reservasCliente)

    def mostrarReserva(self, reservas):
        
        registro = tk.Toplevel(self)
        registro.title("Reservas del Cliente")
        
        reservas_nombres = [reserva.getCliente().getId() for reserva in reservas]
        
        valor_defecto_reservas = tk.StringVar(value="Reservas")
        combo_style2 = ttk.Style()
        combo_style2.configure('My.TCombobox', padding=[20, 5, 90, 5])
        combo3 = ttk.Combobox(self, values=reservas_nombres, textvariable=valor_defecto_reservas, style='My.TCombobox')
        combo3.grid(row=1, column=1, padx=2, pady=10, sticky="w")

        otro_label3 = tk.Label(self, text="Seleccione su reserva", font=("Arial", 15), bg="white")
        otro_label3.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        nuevo_frame1 = tk.Frame(self)
        nuevo_frame1.grid(row=3, column=0, columnspan=4, pady=10)

        combo3.grid(row=3, column=1, padx=2, pady=10, sticky="w")
        
        



        # boton_guardar = tk.Button(registro, text="Aceptar", height=1, command=lambda: self.mostrarMensaje(entry_id.get(), entry_nm.get(), sedeElegida, mesa, fecha))
        # boton_guardar.pack(pady=20)