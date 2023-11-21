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
from baseDatos import Deserializador,Serializador

dic= {"2023-10-25 14:00 PM":0, "2023-10-25 18:00 PM":1, "2023-10-26 12:00 PM": 2, "2023-10-30 11:00 AM":3}
tipoMesa = ["Dos personas", "Tres personas", "Cuatro o más personas"]



class Fechasreserv(tk.Frame): 
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        
        self.controlador = controlador
        self.configure(background="white")
        

        label1 = tk.Label(self, justify=CENTER, text="Generación de Reservas", bg=BACKGROUND_FRAMES, font=("Comic Sans MS", 30), fg="white")
        label1.grid(row=0, column=1, columnspan=2, pady=10)

        valor_defecto = tk.StringVar(value="Fechas")
        combo_style = ttk.Style()

        # Crea un nuevo estilo personalizado (My.TCombobox) y ajusta la altura (padding)
        combo_style.configure('My.TCombobox', padding=[20, 5, 90, 5])
        combo1 = ttk.Combobox(self, values=["2023-10-25 14:00 PM", "2023-10-25 18:00 PM", "2023-10-26 12:00 PM", "2023-10-30 11:00 AM"], textvariable=valor_defecto,
                             style='My.TCombobox', state="readonly")
        combo1.grid(row=1, column=1, padx=2, pady=10, sticky="w")

        otro_label = tk.Label(self, text="Seleccionar Fecha ", bg=BACKGROUND_FRAMES, font=("Comic Sans MS", 20), fg="white")
        otro_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        nuevo_frame = tk.Frame(self)
        nuevo_frame.grid(row=2, column=0, columnspan=4, pady=10)
        
        valor_defecto = tk.StringVar(value="Mesas")
        combo_style = ttk.Style()

        # Crea un nuevo estilo personalizado (My.TCombobox) y ajusta la altura (padding)
        combo_style.configure('My.TCombobox', padding=[20, 5, 90, 5])
        combo2 = ttk.Combobox(self, values=["Dos personas", "Tres personas", "Cuatro o más personas"], textvariable=valor_defecto,
                             style='My.TCombobox', state="readonly")
        combo2.grid(row=2, column=1, padx=2, pady=10, sticky="w")

        otro_label2 = tk.Label(self, text="Seleccionar Mesa ", bg=BACKGROUND_FRAMES, font=("Comic Sans MS", 20), fg="white")
        otro_label2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        nuevo_frame1 = tk.Frame(self)
        nuevo_frame1.grid(row=2, column=0, columnspan=4, pady=10)
        
        boton = tk.Button(self, text="Aceptar", height=1, command=lambda: self.aceptarOP(combo1.get(), combo2.get()))
        boton.grid(row=2, column=2, padx=2, sticky="w")
        
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
        valor_defecto_sedes = tk.StringVar(value="Sedes")
        combo_style2 = ttk.Style()
        combo_style2.configure('My.TCombobox', padding=[20, 5, 90, 5])
        combo3 = ttk.Combobox(self, values=sede_nombres, textvariable=valor_defecto_sedes, style='My.TCombobox', state="readonly")
        combo3.grid(row=1, column=1, padx=2, pady=10, sticky="w")

        otro_label3 = tk.Label(self, text="Seleccionar Sede ", bg=BACKGROUND_FRAMES, font=("Comic Sans MS", 20), fg="white")
        otro_label3.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        nuevo_frame1 = tk.Frame(self)
        nuevo_frame1.grid(row=3, column=0, columnspan=4, pady=10)

        combo3.grid(row=3, column=1, padx=2, pady=10, sticky="w")
        
        boton = tk.Button(self, text="Aceptar", height=1, command=lambda: self.reservacionPro(fecha, combo3.get(), mesa))
        boton.grid(row=3, column=2, padx=2, sticky="w")
   
    def reservacionPro(self, fecha, sedeElegida, mesa):
        
        for reserva in Reserva.listaReservas:
            if reserva.getFecha() == fecha  and reserva.getMiSede() == sedeElegida:
                messagebox.showinfo( "Advertencia","Ya está reservado")
                return   
        
        self.registadoCliente(fecha, sedeElegida, mesa)
    
    def registadoCliente(self, fecha, sedeElegida, mesa):
        registro = tk.Toplevel(self)
        registro.title("Registro de Cliente")

        label_id = tk.Label(registro, text="Digite su ID", font=("Arial", 15))
        label_id.pack(pady=10)

        self._entry_id = tk.Entry(registro, width=40)
        self._entry_id.focus_set()
        self._entry_id.pack()
        
        label_nombre = tk.Label(registro, text="Digite su nombre", font=("Arial", 15))
        label_nombre.pack(pady=10)

        self._entry_nm = tk.Entry(registro, width=40)
        self._entry_nm.focus_set()
        self._entry_nm.pack()

        boton_guardar = tk.Button(registro, text="Aceptar", height=1, command=lambda: self.mostrarMensaje(self._entry_id.get(), self._entry_nm.get(), sedeElegida, mesa, fecha))
        boton_guardar.pack(pady=20)
        
        
    def mostrarMensaje(self, id,nombre, sedeElegida, mesa, fecha):
        clienteId = self._entry_id.get()
        try:
            nombreCliente = Cliente.buscarCliente(int(clienteId)).getNombre()
            platoPreferido = Cliente.buscarPlatoPreferido(int(clienteId))
        except:
            messagebox.showerror("Error", "El id ingresado no es válido")
            return
        
        miCliente = Cliente(nombre,id)
        miReserva = Reserva(miCliente, sedeElegida, mesa, fecha)
        Serializador.agregarReservaNueva(miReserva) 
        messagebox.showinfo("Información", miReserva.__str__())

       
        