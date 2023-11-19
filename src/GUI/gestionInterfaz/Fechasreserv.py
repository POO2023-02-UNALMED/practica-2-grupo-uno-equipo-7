import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.inventarioaply import Inventarioaply
from gestorAplicacion.Restaurante import Restaurante
dic= {"2023-10-25 14:00 PM":0, "2023-10-25 14:00 PM":1, "2023-10-26 12:00 PM": 2, "2023-10-30 11:00 AM":3}




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
        combo = ttk.Combobox(self, values=["2023-10-25 14:00 PM", "2023-10-25 14:00 PM", "2023-10-26 12:00 PM", "2023-10-30 11:00 AM"], textvariable=valor_defecto,
                             style='My.TCombobox')
        combo.grid(row=1, column=1, padx=2, pady=10, sticky="w")

        otro_label = tk.Label(self, text="Seleccionar Fecha ", font=("Arial", 20), bg="white")
        otro_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        nuevo_frame = tk.Frame(self)
        nuevo_frame.grid(row=2, column=0, columnspan=4, pady=10)
        


        
    
