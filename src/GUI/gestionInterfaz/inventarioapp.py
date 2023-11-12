import tkinter as tk
from tkinter import ttk

class Inventarioaply:  # Simulando la implementación de Inventarioaply
    pass

class Item:  # Simulando la implementación de Item
    pass

class Restaurante:  # Simulando la implementación de Restaurante
    pass

class inventarioapp(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.configure(background="white")

        label1 = tk.Label(self, text="Inventario", font=("Arial", 40), fg="pink")
        label1.grid(row=0, column=2, columnspan=2, pady=10)

        valor_defecto = tk.StringVar(value="Sedes")
        combo_style = ttk.Style()

        # Crea un nuevo estilo personalizado (My.TCombobox) y ajusta la altura (padding)
        combo_style.configure('My.TCombobox', padding=[20, 5, 90, 5])
        combo = ttk.Combobox(self, values=["envigado", "sandiego", "La Amercia", "belen"], textvariable=valor_defecto,
                             style='My.TCombobox')
        combo.grid(row=1, column=1, padx=2, pady=10, sticky="w")

        otro_label = tk.Label(self, text="Seleccionar sede ", font=("Arial", 20), bg="white")
        otro_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        boton = tk.Button(self, text="Select", height=1, command=lambda: self.inventario2(combo.get()))
        boton.grid(row=1, column=2, padx=2, sticky="w")
        nuevo_frame = tk.Frame(self)
        nuevo_frame.grid(row=2, column=0, columnspan=4, pady=10)

        # Agrega una etiqueta con el nombre de la sede
        self.label_sede = tk.Label(nuevo_frame, text=f"", font=("Arial", 20), bg="white")
        self.label_sede.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Crea un nuevo Frame para mostrar el nombre de la sede seleccionada
        
        
       
        
        

    def inventario2(self, nombre_sede):
        self.label_sede.config(text=f"Sede seleccionada: {nombre_sede}")
        
        
        # Crea un nuevo Frame para mostrar el nombre de la sede seleccionada
        
        
    
        
        
        
        
        
        
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
    
    