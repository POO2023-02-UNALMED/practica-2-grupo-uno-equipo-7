import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.inventarioaply import Inventarioaply
from gestorAplicacion.Restaurante import Restaurante
from gestorAplicacion.Mesa import *
dic= {"2023-10-25 14:00 PM":0, "2023-10-25 14:00 PM":1, "2023-10-26 12:00 PM": 2, "2023-10-30 11:00 AM":3}
tipoMesa = ["Dos personas", "Tres personas", "Cuatro o más personas"]



class Fechasreserv(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.configure(background="white")

        label1 = tk.Label(self, text="Generación de Reservas", font=("Arial", 40), fg="black")
        label1.grid(row=0, column=2, columnspan=2, pady=10)

        valor_defecto = tk.StringVar(value="Fechas")
        combo_style = ttk.Style()

        # Crea un nuevo estilo personalizado (My.TCombobox) y ajusta la altura (padding)
        combo_style.configure('My.TCombobox', padding=[20, 5, 90, 5])
        combo1 = ttk.Combobox(self, values=["2023-10-25 14:00 PM", "2023-10-25 14:00 PM", "2023-10-26 12:00 PM", "2023-10-30 11:00 AM"], textvariable=valor_defecto,
                             style='My.TCombobox')
        combo1.grid(row=1, column=1, padx=2, pady=10, sticky="w")

        otro_label = tk.Label(self, text="Seleccionar Fecha ", font=("Arial", 20), bg="white")
        otro_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        nuevo_frame = tk.Frame(self)
        nuevo_frame.grid(row=2, column=0, columnspan=4, pady=10)
        
        valor_defecto = tk.StringVar(value="Mesas")
        combo_style = ttk.Style()

        # Crea un nuevo estilo personalizado (My.TCombobox) y ajusta la altura (padding)
        combo_style.configure('My.TCombobox', padding=[20, 5, 90, 5])
        combo2 = ttk.Combobox(self, values=["Dos personas", "Tres personas", "Cuatro o más personas"], textvariable=valor_defecto,
                             style='My.TCombobox')
        combo2.grid(row=2, column=1, padx=2, pady=10, sticky="w")

        otro_label2 = tk.Label(self, text="Seleccionar Mesa ", font=("Arial", 20), bg="white")
        otro_label2.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        
        nuevo_frame1 = tk.Frame(self)
        nuevo_frame1.grid(row=2, column=0, columnspan=4, pady=10)
        
        boton = tk.Button(self, text="Aceptar", height=1, command=lambda: self.aceptarOP(combo1.get(), combo2.get()))
        boton.grid(row=1, column=2, padx=2, sticky="w")
        
    def aceptarOP(self, fecha, mesa):
        
        mesasEncontradas = Mesa.mesasDisponibles(mesa)
        horariosEncontrados = Restaurante.horarios_disponibles(fecha)
        sedesEncontradas = []
        
        for restaurante in horariosEncontrados:
            for mesa in mesasEncontradas:
                if (mesa.getUbicacion() == restaurante.get_ubicacion()):
                    sedesEncontradas.append(restaurante)