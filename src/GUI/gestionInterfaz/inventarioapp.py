import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import ttk

class inventarioapp(Frame):
    def __init__(self, padre,  controlador):
        super().__init__(padre)
        self.controlador=controlador
        self.configure(background="white")
        label1=tk.Label(self, text="Inventario", font=("Arial",40),fg="pink")
        label1.grid(row=0, column=2, columnspan=2, pady=10)
        valor_defecto=tk.StringVar(value="Sedes")
        combo_style = ttk.Style()
        
        # Crea un nuevo estilo personalizado (My.TCombobox) y ajusta la altura (padding)
        combo_style.configure('My.TCombobox', padding=[20, 5, 90, 5])
        combo=ttk.Combobox(self, values=["envigado","sandiego","La Amercia", "belen"], textvariable=valor_defecto,style='My.TCombobox')
        combo.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        otro_label = tk.Label(self, text="seleccionar sede ", font=("Arial", 20),bg="white")
        otro_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        
        
        
        
    
    