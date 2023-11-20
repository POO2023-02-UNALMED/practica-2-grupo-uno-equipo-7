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

dic= {"2023-10-25 14:00 PM":0, "2023-10-25 18:00 PM":1, "2023-10-26 12:00 PM": 2, "2023-10-30 11:00 AM":3}
tipoMesa = ["Dos personas", "Tres personas", "Cuatro o más personas"]


class ModificarRes(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background="white")
        self._controlador = controlador
        
        self._inicializarTitulo()
        self._inicializarEntrada()
        
    def _inicializarTitulo(self):    

        # Se inicializa el título  que va a estar en la parte superior de la ventana
        labelInicial = Label(self, justify=CENTER, text="Modificar Reservación", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
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

            if (int(reserva.getCliente().getId()) == int(id)):
                reservasCliente.append(reserva)
                
        
        self.mostrarReserva(reservasCliente)

    def mostrarReserva(self, reservas):
        
        # Se inicializa el desplegable para mostrar los platos recomendados para el cliente
        self._desplegable = Combobox(self, state="readonly", font=FONT2)
        self._desplegable.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        self._desplegable.configure(values=reservas)
        self._desplegable.set("Seleccione su reservación")
        boton_cancelar = tk.Button(self, text="Modificar", height=1, command=lambda: self.modificar_reserva(self._desplegable.get()))
        boton_cancelar.pack(pady=20)

        
    def modificar_reserva(self, reservaModificar):
        
        # Se inicializa el desplegable de fecha
        self._desplegable1 = Combobox(self, state="readonly", font=FONT2)
        self._desplegable1.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        self._desplegable1.configure(values=["2023-10-25 14:00 PM", "2023-10-25 18:00 PM", "2023-10-26 12:00 PM", "2023-10-30 11:00 AM"])
        self._desplegable1.set("Seleccione la nueva fecha")
        
        # Se inicializa el desplegable de mesa
        self._desplegable2 = Combobox(self, state="readonly", font=FONT2)
        self._desplegable2.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        self._desplegable2.configure(values=["Dos personas", "Tres personas", "Cuatro o más personas"])
        self._desplegable2.set("Seleccione el nuevo tipo de mesa")
        boton_aceptar = tk.Button(self, text="Aceptar", height=1, command=lambda: self.aceptarOP(self._desplegable1.get(),  self._desplegable2.get()))
        boton_aceptar.pack(pady=20)
        
    def aceptarOP(self, fecha, mesa):
        sedesEncontradas = []   
        mesasEncontradas = Mesa.mesasDisponibles(mesa)
        horariosEncontrados = Restaurante.horarios_disponibles(fecha)
        
        horariosEncontrados = list( set( horariosEncontrados ) )

        
        for restaurante in horariosEncontrados:
            for mesa in mesasEncontradas:
                if (mesa.getUbicacion() == restaurante.get_ubicacion()):
                    sedesEncontradas.append(restaurante)
        
        if(len(sedesEncontradas) == 0):
            messagebox.showerror("Error", "No se encontraron sedes disponibles según su requerimiento")
        else:
            self.mostrarSedes(sedesEncontradas, fecha, mesa)

    
    
    def mostrarSedes(self, sedesEncontradas, fecha, mesa):

        sede_nombres = [restaurante.get_ubicacion() for restaurante in sedesEncontradas]

        
        # Se inicializa el desplegable para mostrar los platos recomendados para el cliente
        self._desplegable = Combobox(self, state="readonly", font=FONT2)
        self._desplegable.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        self._desplegable.configure(values=sede_nombres)
        self._desplegable.set("Seleccione la sede deseada")
        boton_cancelar = tk.Button(self, text="Aceptar", height=1, command=lambda: self.actualizacionRe(self._desplegable1.get(), self._desplegable.get(), self._desplegable2.get() ))
        boton_cancelar.pack(pady=20)

        
    def actualizacionRe(self, fecha, sedeElegida, mesa):

        for reserva in Reserva.listaReservas:
            if reserva.getFecha() == fecha  and reserva.getMiSede() == sedeElegida:
                messagebox.showinfo( "Advertencia","Ya está reservado")
                break 
        self.actualizacion(fecha, sedeElegida, mesa)
        
    def actualizacion(self, fecha, sedeElegida, mesa):
        nuevaReserva = None
        for reserva in Reserva.listaReservas:
            print(reserva.getMiSede(), sedeElegida)
            if (reserva.getMiSede() == sedeElegida):
                nuevaReserva = reserva
            
                
        # nuevaReserva.setFecha(fecha) 
        # nuevaReserva.setMiSede(sedeElegida)
        # nuevaReserva.setMiMesa(mesa) 
        
        # messagebox.showinfo( "Información", nuevaReserva.__str__())      
        